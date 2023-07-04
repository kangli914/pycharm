#!/usr/bin/env python3

import concurrent.futures
import logging
import os
import random
import string
import sys
import time
from datetime import datetime
from itertools import cycle
from multiprocessing import Process

import pandas
import psycopg2
import pymongo
import requests
# from graphviz import render
from matplotlib import pyplot
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from treelib import Node, Tree

"""Build a catalog in PCM with a deterministic tree structure consists of hierachies, nodes and products."""

HIERARCHIES = int(sys.argv[1])                      # the number hierarchies to create
MAX_DEPTH = int(sys.argv[2])                        # the number of egdes from root node to a leaf node (so expecting value > 0)
WIDTH = int(sys.argv[3])                            # the number of children a node has
TOTAL_PRODUCTS = int(sys.argv[4])                   # the total number of products to be created
PRODUCTS_IN_NODE = int(sys.argv[5])                 # the number of products allocated to a node
CATALOG_RULE_NAME = str(sys.argv[6])                # the name of catalog rule used for the publish catalog

TAG = os.getenv("TAG", default="")
if TAG == "":
    TAG = datetime.now().strftime("%Y%m%d%H%M%S")   # the identifier tag for each test

if not CATALOG_RULE_NAME:
    CATALOG_RULE_NAME = str(TAG)

# Environment variables
SERVER = os.getenv("SERVER", default="your server")
CLIENT_ID = os.getenv("CLIENT_ID", default="your client id")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", default="your client secret")
STORE_ID = os.getenv("STORE_ID", default="your store id")

EPCC_ENV = os.getenv("EPCC_ENV", default="your test environment")
JOB_NAME = os.getenv("JOB_NAME", default="your server passed from Jenkins")
RUN_NUMBER = int(os.getenv("RUN_NUMBER", default="your build passed from Jenkins"))
DESCRIPTION = os.getenv("DESCRIPTION", default="your description passed from Jenkins")
DATASET = os.getenv("DATASET", default="your catalog size passed from Jenkins")

METABASE_HOST = os.getenv("METABASE_HOST", default="your metabase postgresql server")
METABASE_USER = os.getenv("METABASE_USER", default="your metabase user")
METABASE_PASSWORD = os.getenv("METABASE_PASSWORD", default="your metabase password")
METABASE_DB = os.getenv("METABASE_DB", default="your metabase database")

MONGO_DNS_CATALOGVIEW = os.getenv("MONGO_DNS_CATALOGVIEW", default="your mongo dns")
MONGO_DNS_PIM = os.getenv("MONGO_DNS_PIM", default="your mongo dns")
MONGO_DNS_PRICEBOOKS = os.getenv("MONGO_DNS_PRICEBOOKS", default="your mongo dns")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", default="your rabbitmq")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT", default="your rabbitmq")
RABBITMQ_VIRTUAL_HOST = os.getenv("RABBITMQ_VIRTUAL_HOST", default="your rabbitmq")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", default="your rabbitmq")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", default="your rabbitmq")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", default="your rabbitmq queue name")
THREAD_NODE = int(os.getenv("THREAD_NODE", default="your total number of threads to create nodes"))
THREAD_PRODUCT = int(os.getenv("THREAD_PRODUCT", default="your total number of threads to create products"))
THREAD_PRICE = int(os.getenv("THREAD_PRICE", default="your total number of threads to create product prices"))
THREAD_PRODUCT2NODE = int(os.getenv("THREAD_PRODUCT2NODE", default="your total number of threads to attach the products to nodes"))
THREAD_BUNDLES = int(os.getenv("THREAD_BUNDLES", default="number of threads to build bundles"))
THREAD_INVENTORY = int(os.getenv("THREAD_INVENTORY", default="number of threads to create inventories"))
BATCH_SIZE_PRODUCT2NODE = int(os.getenv("BATCH_SIZE_PRODUCT2NODE", default="your total number of products to be attached to a node per request"))
PRODUCTS_TEMPLATE_ENABLED = int(os.getenv("PRODUCTS_TEMPLATE_ENABLED", default="extend the PCM products using the flows"))
TOTAL_FILES = int(os.getenv("TOTAL_FILES", default="total number of files to be created"))
NUM_FILES_PER_PRODUCT = int(os.getenv("NUM_FILES_PER_PRODUCT", default="number of files associated with each product"))
NUM_TEMPLATE = int(os.getenv("NUM_TEMPLATE", default="your total number of the PCM Flows templates used to extend the products"))
NUM_FLOW_FIELD = int(os.getenv("NUM_FLOW_FIELD", default="your total number of feilds in the flows"))
NUM_PROMOTION = int(os.getenv("NUM_PROMOTION", default="your total number of promotion"))
NUM_PROMOTION_CODE = int(os.getenv("NUM_PROMOTION_CODE", default="your total number of promotion code for specific promotion"))
NUM_VARIATION = int(os.getenv("NUM_VARIATION", default="extend the PCM products by the number of variations"))
NUM_OPTION = int(os.getenv("NUM_OPTION", default="extend the PCM products by the number of options per variation"))
NUM_BUNDLES = int(os.getenv("NUM_BUNDLES", default="number of bundles to create"))
NUM_PRODUCTS_PER_BUNDLE = int(os.getenv("NUM_PRODUCTS_PER_BUNDLE", default="number of products to add to each bundle"))
INVENTORY_ENABLED = int(os.getenv("INVENTORY_ENABLED", default="flag to indicate whether products should track invetory"))
NUM_INVENTORY = int(os.getenv("NUM_INVENTORY", default="inventory count to add to each product"))
NUM_BASE_PRODUCT = int(os.getenv("NUM_BASE_PRODUCT", default="base product count used to PCM build children products via product variations"))
CORE_CARTS_FLOW_ENABLED = int(os.getenv("CORE_CARTS_FLOW_ENABLED", default="flag to indicate whether create a core flows to extend the carts"))
NUM_CARTS_CORE_FLOW_FIELD = int(os.getenv("NUM_CARTS_CORE_FLOW_FIELD", default="your total number of feilds extended from the core carts flows"))

# Random texts in different bytes size
TEXTS_10_BYTES = "".join(random.choices(string.ascii_letters + string.digits, k=10))
TEXTS_50_BYTES = "".join(random.choices(string.ascii_letters + string.digits, k=50))
TEXTS_100_BYTES = "".join(random.choices(string.ascii_letters + string.digits, k=100))
TEXTS_500_BYTES = "".join(random.choices(string.ascii_letters + string.digits, k=500))
TEXTS_1_KB = "".join(random.choices(string.ascii_letters + string.digits, k=1000))
TEXTS_5_KB = "".join(random.choices(string.ascii_letters + string.digits, k=5000))
TEXTS_10_KB = "".join(random.choices(string.ascii_letters + string.digits, k=10000))
TEXTS_APPENDER = dict(xxsmall=TEXTS_10_BYTES, xsmall=TEXTS_50_BYTES, small=TEXTS_100_BYTES, medium=TEXTS_500_BYTES, large=TEXTS_1_KB, xlarge=TEXTS_5_KB, xxlarge=TEXTS_10_KB)

# Store the authentication token
token = dict()
# Flows palce holder
flows = {}
# Variations place holder
variations = []


def setup_logger(name, file, formatter, level=logging.INFO):
    """Setup the basic loggers."""

    file_handler = logging.FileHandler(file)
    format = logging.Formatter(formatter, datefmt="%Y-%m-%d %H:%M:%S")
    file_handler.setFormatter(format)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)

    # log to console for perflog logger only
    if name == "perlog":
        console = logging.StreamHandler()
        console.setFormatter(format)
        logger.addHandler(console)

    return logger


# for build out log for everything
detail_logger = setup_logger("perlog", "perflab_debug.log", "[%(asctime)s]: [%(levelname)s]: %(message)s")
# for transaction metric log
txn_summary_logger = setup_logger("txn_summary", "summary.log", "%(message)s")


# Setup Retry strategy
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    # status_forcelist=[429, 500, 502, 504],
    allowed_methods=["HEAD", "GET", "PUT", "POST", "OPTIONS"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)


# Store the specific properties that a node have and it can grow later.
# Currently it stores the depth of node and the number of products attached to the node.
class NodeProperties():
    def __init__(self, depth: int, products: int):
        self.depth = depth
        self.products = products

    def get_depth(self):
        return self.depth

    def get_product_cnt(self):
        return self.products

    def update_products_cnt(self, new: int):
        self.products = new


def get_authorized_token():
    """Get the authorized token.

    It updates the token string and expired time in memory (i.e. a token dictionary) and then it returns the access token string.
    """

    r = http.post(SERVER + "/oauth/access_token", data={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "grant_type": "client_credentials"})
    r.raise_for_status()

    token["access_token"] = "Bearer " + r.json()["access_token"]
    token["expire"] = r.json()["expires"]
    readable_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(token["expire"]))

    detail_logger.debug(f"Returned the access token: {token['access_token']}, expire at Epoch time: {token['expire']} or Local time: {readable_time}")

    return token["access_token"]


def validate_token():
    """Validate the current token obtained from the last authorization.

    If current token is about to expire in 5 minutes (current default) then it obtains a new token,
    otherwise it returns the current token since it is still valid.
    """

    current_time = int(time.time())
    expire_time = token["expire"]
    gap = 300

    # renew the token as it is about to expire in 5 minutes
    if ((expire_time - current_time) < gap):
        detail_logger.debug("Current token is about to expire and need to get a new token")
        get_authorized_token()

    return token["access_token"]


def get_headers(token: str):
    """Return the header."""

    return {
        "Content-Type": "application/json",
        "Authorization": token,
        "EP-Internal-unlimited": "true",
        "EP-Perf-Unlimited": "true",
        "X-Moltin-Auth-Store": STORE_ID,
    }


def create_hierarchy_tree(hierarchy_id: str, nodes_ids: list):
    """Build a data strcuture for the product hierachy tree."""

    hierarchy = Tree()
    parent_nodes_ids = []
    # children_nodes_ids = []

    # Series to store the transaction metrics for the node relationships api calls
    elapsed_times = pandas.Series(dtype="float64")
    tps = pandas.Series(dtype="float64")
    bytes_received = pandas.Series(dtype="float64")
    error_count = 0

    start = time.time_ns()
    for d in range(MAX_DEPTH + 1):
        # hierachy at root level (e.g. depth = 0)
        if d == 0:
            # assume no product will be attached to the hierachy root node
            hierarchy.create_node("hierarchy", hierarchy_id, data=NodeProperties(d, 0))
            parent_nodes_ids.append(hierarchy_id)
        else:
            children_nodes = []
            # children_nodes_ids.clear()
            # formed a list of children nodes at dth level in depth
            for _ in range(WIDTH**d):
                id = nodes_ids.pop()
                node = Node(tag="node", identifier=id, data=NodeProperties(d, PRODUCTS_IN_NODE))
                children_nodes.append(node)
            children_nodes_ids = [node.identifier for node in children_nodes]

            # creating nodes relationship at current level
            for parent in parent_nodes_ids:
                children_ids = []
                for _ in range(WIDTH):
                    child_node = children_nodes.pop()
                    hierarchy.add_node(child_node, parent)
                    children_ids.append(child_node.identifier)
                if (parent != hierarchy_id):
                    response_status, tps_per_thread, elapsed_ms, response_bytes = create_node_relationships(hierarchy_id, parent, children_ids)

                    # store transaction metrics in series
                    elapsed_times = elapsed_times.append(elapsed_ms, ignore_index=True)
                    tps = tps.append(tps_per_thread, ignore_index=True)
                    bytes_received = bytes_received.append(response_bytes, ignore_index=True)

                    if response_status not in (200, 201):
                        error_count += 1

            parent_nodes_ids = children_nodes_ids

    finish = time.time_ns()
    elapsed_sec = (finish - start) / 1000000000

    detail_logger.info(f"Formed a hierarchy tree nodes of {MAX_DEPTH} depth and {WIDTH} width in {str(round(elapsed_sec, 2))} seconds")

    # log and wirte the node relationship calls only of edge is more than 1.
    # If edge is equal to 1 then the nodes will be under hierarchy automically as part of the node creation
    if (MAX_DEPTH > 1):
        txn_summary = init_transaction_metric()
        update_transaction_metric(txn_summary,
                                  transactionName="UT_AttachNode",
                                  timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                                  timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                                  virtualUsers=1,
                                  transactionCount=elapsed_times.size,
                                  transactionsPerSecond=round(tps.mean(), 2),
                                  responseTimeMin=round(elapsed_times.min()),
                                  responseTimeAverage=round(elapsed_times.mean()),
                                  responseTimeMax=round(elapsed_times.max()),
                                  responseTimeMedian=round(elapsed_times.median()),
                                  responseTime90thPercentile=round(elapsed_times.quantile(0.9)),
                                  responseTime95thPercentile=round(elapsed_times.quantile(0.95)),
                                  apdex=apdex(elapsed_times),
                                  byteSizeMin=round(bytes_received.min()),
                                  byteSizeAverage=round(bytes_received.mean()),
                                  byteSizeMax=round(bytes_received.max()),
                                  errorsTotal=error_count,
                                  errorsPercent=round(error_count / elapsed_times.size, 2),
                                  stepDuration=str(round(elapsed_sec))
                                  )
        log_transaction_metric(txn_summary)
        write_transaction_metabase(txn_summary)

    return hierarchy


def show(tree: Tree, **kwargs):
    """Show the hierarchy nodes and the products allocation to the node."""

    print()
    print("hierarchy tree with node ids:")
    print("------")
    tree.show(idhidden=False)

    if "data_property" in kwargs:
        print("products allocation among the nodes:")
        print("------")
        tree.show(data_property="products")

    print("Type | Node id | Parent node id")
    print("------")
    for node in tree.all_nodes():
        if not node.is_root():
            print(node.tag, node.identifier, tree.parent(node.identifier).identifier)
    print()

    print(f"total nodes: {tree.size()} walking through the order from top to buttom")
    print("------")
    print(','.join([str(tree[node].identifier) for node in tree.expand_tree(mode=Tree.ZIGZAG)]))
    print()


# def draw(tree: Tree):
#     """Generate the image file."""
#     tree.to_graphviz("tree.dot")
#     render('dot', 'png', 'tree.dot')


def track_latency(elapsed_times: pandas.Series, title: str, xlabel: str, ylabel: str, fname: str):
    """Plot the chart to track the endpoint latency and save it to png files"""

    path = os.getcwd()

    ax = elapsed_times.plot(kind="line", color="mediumvioletred")
    addon = f"\n [average: {int(elapsed_times.mean())} ms; maximum: {int(elapsed_times.max())} ms; total reqs {elapsed_times.size}]"
    ax.set_title(title + addon, color="blue", fontsize=10)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    pyplot.savefig(f"{path}/tmp/{fname}-latnecy.png")
    # pyplot.show()
    pyplot.clf()


def apdex(results: pandas.Series):
    """Calculate Apdex score (application performance index) for transaction."""

    # To-Do: define rule to handle asynchronous long transactions
    T = 300
    Multiplier = 3

    satisfied_count = 0
    tolerated_count = 0

    for item in results:
        if item <= T:
            satisfied_count += 1
        if T < item <= Multiplier * T:
            tolerated_count += 1

    apdex_score = round((satisfied_count + tolerated_count / 2) / results.size, 2)
    return apdex_score


def init_transaction_metric():
    """Initilize the value for transaction summary."""

    # Inial value for the ransaction summary metrics
    return dict(job=JOB_NAME,
                runNumber=RUN_NUMBER,
                timeStart=None,
                timeStop=None,
                product="EPCC",
                productBranch=None,
                deployBranch=None,
                dockerBranch=None,
                testType="Constant",
                testName="build_new_catalog",
                transactionName=None,
                environment=EPCC_ENV,
                build=None,
                dataset=DATASET,
                description=DESCRIPTION,
                isPeak=True,
                virtualUsers=1,
                transactionCount=0,
                transactionsPerSecond=0.00,
                responseTimeMin=0,
                responseTimeAverage=0,
                responseTimeMax=0,
                responseTimeMedian=0,
                responseTime90thPercentile=0,
                responseTime95thPercentile=0,
                apdex=0.00,
                byteSizeMin=0,
                byteSizeAverage=0,
                byteSizeMax=0,
                errorsTotal=0,
                errorsPercent=0.00,
                project="Build EPCC PCM Catalog",
                stepDuration=None
                )


def update_transaction_metric(txn_summary: dict, **kwargs):
    """Update the transaction summary values."""

    for key, value in kwargs.items():
        txn_summary[key] = value


def log_transaction_metric(txn_summary: dict):
    """Log the transaction metric to the summary file."""

    txn_summary_logger.info(",".join(str(item) for item in txn_summary.values()))


def write_transaction_metabase(txn_summary: dict):
    """Write transaction summary metric to metabase postgresql database only if it's running against Staging."""

    if EPCC_ENV == "Staging":
        try:
            connection = psycopg2.connect(user=METABASE_USER, password=METABASE_PASSWORD, host=METABASE_HOST, port="5432", database=METABASE_DB)
            cursor = connection.cursor()

            key = ", ".join(txn_summary.keys())
            position = ", ".join(['%s'] * len(txn_summary))

            # insert given transaction metrics into the metabase
            insert_query = "INSERT INTO jmeterResults (%s) VALUES (%s)" % (key, position)
            cursor.execute(insert_query, list(txn_summary.values()))
            connection.commit()

            detail_logger.debug(f"Transaction [{txn_summary.get('transactionName')}] metrics inserted to the Metabase successfully")
        except (Exception, psycopg2.Error) as e:
            detail_logger.error(f"Error while connecting to Metabase PostgreSQL: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()
                detail_logger.debug("Metabase PostgreSQL connection is closed")


def get_num_nodes(depth=MAX_DEPTH, width=WIDTH):
    """Get a total number of nodes including the root (e.g. hierarchy node) given the maxium depth and the width"""

    node_cnt = 0
    for d in range(depth + 1):
        node_cnt += WIDTH**d

    return node_cnt


def create_hierarchy():
    """Create a hierachy."""

    error_count = 0
    data = {
        "data": {
            "type": "hierarchy",
            "attributes": {
                "name": "perf hierarchy {}".format(TAG),
                "description": "Hierarchy {} perflab test data {}".format(TAG, TEXTS_APPENDER["small"]),
                "slug": "perf-slug-{}".format(TAG)
            }
        }
    }
    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/hierarchies", headers=headers, json=data)
    finish = time.time_ns()

    # get reponse status
    response_status = r.status_code
    if response_status not in (200, 201):
        error_count += 1
    r.raise_for_status()

    hierarchy_id = r.json()["data"]["id"]
    # get response bytes
    response_bytes = len(r.content)
    elapsed_ms = (finish - start) / 1000000
    detail_logger.info(f"Created a hierachy; hierachy id: {hierarchy_id} in {str(round(elapsed_ms, 2))} miliseconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_CreateHierarchy",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=1,
                              transactionCount=1,
                              transactionsPerSecond=round(1000 / elapsed_ms, 2),
                              responseTimeMin=round(elapsed_ms),
                              responseTimeAverage=round(elapsed_ms),
                              responseTimeMax=round(elapsed_ms),
                              responseTimeMedian=round(elapsed_ms),
                              responseTime90thPercentile=round(elapsed_ms),
                              responseTime95thPercentile=round(elapsed_ms),
                              apdex=apdex(pandas.Series([elapsed_ms])),
                              byteSizeMin=round(response_bytes),
                              byteSizeAverage=round(response_bytes),
                              byteSizeMax=round(response_bytes),
                              errorsTotal=error_count,
                              errorsPercent=round(float(error_count), 2),
                              stepDuration=str(round(elapsed_ms / 1000))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)

    return hierarchy_id


def create_node(hierarchy_id: str, node_idx: int, node_text=""):
    """Create a node under a given hierachy."""

    data = {
        "data": {
            "type": "node",
            "attributes": {
                "name": "perf node {}_{}".format(node_idx + 1, TAG),
                "description": "Node {}_{} perflab test data {}".format(node_idx + 1, TAG, node_text),
                "slug": "perf-slug-{}_{}".format(node_idx + 1, TAG)
            }
        }
    }
    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/hierarchies/{hierarchy_id}/nodes", headers=headers, json=data)
    finish = time.time_ns()

    r.raise_for_status()
    node_id = r.json()["data"]["id"]
    elapsed_ms = (finish - start) / 1000000

    # get response bytes
    response_bytes = len(r.content)
    # get reponse status
    response_status = r.status_code

    detail_logger.debug(f"Created a node in {str(round(elapsed_ms, 2))} miliseconds")

    return node_id, response_status, pandas.Series([1000 / elapsed_ms]), pandas.Series([elapsed_ms]), pandas.Series([response_bytes])


def create_node_relationships(hierarchy_id: str, parent_node_id: str, children_nodes_ids: list):
    """Create a node to node(s) relationship.

    Make parent_node_id as the parent of the children nodes in children_nodes_ids list.
    """

    children = []
    for node_id in children_nodes_ids:
        child = {"type": "node"}
        child["id"] = node_id
        children.append(child)
    data = {}
    data["data"] = children

    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/hierarchies/{hierarchy_id}/nodes/{parent_node_id}/relationships/children", headers=headers, json=data)
    finish = time.time_ns()

    r.raise_for_status()
    elapsed_ms = (finish - start) / 1000000
    # get response bytes
    response_bytes = len(r.content)
    # get reponse status
    response_status = r.status_code

    detail_logger.debug(f"Created a node2node relationships (size) [1 parent: {len(children_nodes_ids)} children] in {str(round(elapsed_ms, 2))} miliseconds")

    return response_status, pandas.Series([1000 / elapsed_ms]), pandas.Series([elapsed_ms]), pandas.Series([response_bytes])


def create_product_relationships(hierarchy_id: str, node_id: str, products_pool: cycle, prodcuts_size: int):
    """Create a node to product(s) relationship.

    Allocate a list of products using an cyclist iterator on products pool to a node. The number (size) of products attached
    to a specific node is set by prodcuts_size
    """

    BATCH_SIZE_PRODUCT2NODE = 100
    SLEEP_TIME = 0

    elapsed_times = pandas.Series(dtype="float64")
    tps = pandas.Series(dtype="float64")
    bytes_received = pandas.Series(dtype="float64")
    error_count = 0

    # Batch the request with BATCH_SIZE_PRODUCT2NODE products due to PIM service performance reason
    if prodcuts_size >= BATCH_SIZE_PRODUCT2NODE:

        batch = int(prodcuts_size / BATCH_SIZE_PRODUCT2NODE)
        reminder = prodcuts_size % BATCH_SIZE_PRODUCT2NODE

        for _ in range(batch):
            products = []
            for _ in range(BATCH_SIZE_PRODUCT2NODE):
                product = {"type": "product"}
                # first element of products_pool is the product id, which is used to create node relationship
                product["id"] = next(products_pool)[0]
                products.append(product)

            data = {}
            data["data"] = products
            access_token = validate_token()
            headers = get_headers(access_token)

            start = time.time_ns()
            r = http.post(f"{SERVER}/pcm/hierarchies/{hierarchy_id}/nodes/{node_id}/relationships/products", headers=headers, json=data)
            finish = time.time_ns()

            r.raise_for_status()
            elapsed_ms = (finish - start) / 1000000

            # get response bytes
            response_bytes = len(r.content)
            # get reponse status
            response_status = r.status_code

            detail_logger.debug(f"Created a node2product(s) relationships [(size) 1 node: {BATCH_SIZE_PRODUCT2NODE} product(s)] in {str(round(elapsed_ms, 2))} miliseconds")

            if response_status not in (200, 201):
                error_count += 1
            elapsed_times = elapsed_times.append(pandas.Series([elapsed_ms]), ignore_index=True)
            tps = tps.append(pandas.Series([1000 / elapsed_ms]), ignore_index=True)
            bytes_received = bytes_received.append(pandas.Series([response_bytes]), ignore_index=True)

            time.sleep(SLEEP_TIME)

        if reminder:
            products = []
            for _ in range(reminder):
                product = {"type": "product"}
                # first element of products_pool is the product id, which is used to create node relationship
                product["id"] = next(products_pool)[0]
                products.append(product)

            data = {}
            data["data"] = products

            access_token = validate_token()
            headers = get_headers(access_token)

            start = time.time_ns()
            r = http.post(f"{SERVER}/pcm/hierarchies/{hierarchy_id}/nodes/{node_id}/relationships/products", headers=headers, json=data)
            finish = time.time_ns()

            r.raise_for_status()
            elapsed_ms = (finish - start) / 1000000

            # get response bytes
            response_bytes = len(r.content)
            # get reponse status
            response_status = r.status_code

            detail_logger.debug(f"Created a node2product(s) relationships [(size) 1 node: {reminder} product(s)] in {str(round(elapsed_ms, 2))} miliseconds")

            if response_status not in (200, 201):
                error_count += 1
            elapsed_times = elapsed_times.append(pandas.Series([elapsed_ms]), ignore_index=True)
            tps = tps.append(pandas.Series([1000 / elapsed_ms]), ignore_index=True)
            bytes_received = bytes_received.append(pandas.Series([response_bytes]), ignore_index=True)

    else:
        products = []
        for _ in range(prodcuts_size):
            product = {"type": "product"}
            # first element of products_pool is the product id, which is used to create node relationship
            product["id"] = next(products_pool)[0]
            products.append(product)

        data = {}
        data["data"] = products

        access_token = validate_token()
        headers = get_headers(access_token)

        start = time.time_ns()
        r = http.post(f"{SERVER}/pcm/hierarchies/{hierarchy_id}/nodes/{node_id}/relationships/products", headers=headers, json=data)
        finish = time.time_ns()

        r.raise_for_status()

        # get response bytes
        response_bytes = len(r.content)
        # get reponse status
        response_status = r.status_code

        elapsed_ms = (finish - start) / 1000000
        detail_logger.debug(f"Created a node2product(s) relationships [(size) 1 node: {prodcuts_size} product(s)] in {str(round(elapsed_ms, 2))} miliseconds")

        if response_status not in (200, 201):
            error_count += 1
        elapsed_times = elapsed_times.append(pandas.Series([elapsed_ms]), ignore_index=True)
        tps = tps.append(pandas.Series([1000 / elapsed_ms]), ignore_index=True)
        bytes_received = bytes_received.append(pandas.Series([response_bytes]), ignore_index=True)

    return error_count, tps, elapsed_times, bytes_received


def populate_products_in_node(hierarchy_id: str, nodes: list, products_pool: cycle, workers=2, latency=False):
    """Multi-threaded caller to create_product_relationships() to allocate a list of created products to the nodes.

    Default worker threads is set to 2 and the products pool is iterable among all the nodes.
    """
    elapsed_times = pandas.Series(dtype="float64")
    tps = pandas.Series(dtype="float64")
    bytes_received = pandas.Series(dtype="float64")
    error_count = 0

    start = time.time_ns()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        # only if submitting the request when the node has the products count specified.
        results = [executor.submit(create_product_relationships, hierarchy_id, node.identifier, products_pool, node.data.get_product_cnt()) for node in nodes if node.data.get_product_cnt() != 0]
        for future in concurrent.futures.as_completed(results):
            try:
                error_count_per_thread, tps_per_thread, elapsed_ms_per_thread, response_bytes_per_thread = future.result()

                elapsed_times = elapsed_times.append(elapsed_ms_per_thread, ignore_index=True)
                tps = tps.append(tps_per_thread, ignore_index=True)
                bytes_received = bytes_received.append(response_bytes_per_thread, ignore_index=True)
                error_count = error_count + error_count_per_thread

            except Exception as e:
                detail_logger.error(f"Populating the products attached to a node generated an exception: {e}")
            else:
                # detail_logger.info(f"Attached all of nodes (size: {len(nodes)}) with the products") ### do nothing
                pass
    finish = time.time_ns()
    elapsed_sec = (finish - start) / 1000000000
    detail_logger.info(f"Populated a total of {len(nodes)} nodes with the products allocated in {str(round(elapsed_sec, 2))} seconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_AttachProduct",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=workers,
                              transactionCount=elapsed_times.size,
                              transactionsPerSecond=round(tps.mean() * workers, 2),
                              responseTimeMin=round(elapsed_times.min()),
                              responseTimeAverage=round(elapsed_times.mean()),
                              responseTimeMax=round(elapsed_times.max()),
                              responseTimeMedian=round(elapsed_times.median()),
                              responseTime90thPercentile=round(elapsed_times.quantile(0.9)),
                              responseTime95thPercentile=round(elapsed_times.quantile(0.95)),
                              apdex=apdex(elapsed_times),
                              byteSizeMin=round(bytes_received.min()),
                              byteSizeAverage=round(bytes_received.mean()),
                              byteSizeMax=round(bytes_received.max()),
                              errorsTotal=error_count,
                              errorsPercent=round(error_count / elapsed_times.size, 2),
                              stepDuration=str(round(elapsed_sec))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)

    if latency:
        track_latency(
            elapsed_times, "Products-to-Nodes relationships Latency:\n /pcm/hierarchies/<hierarchy_id>/nodes/<node_id>/relationships/products",
            "requests",
            "latency(ms)",
            "products-2-nodes"
        )


def populate_nodes(hierarchy_id: str, size: int, workers=2, latency=False):
    """Multi-threaded caller to create_node() to create the nodes.

    The number of workers thread is determined by the hosting machine and default is set to 2 threads.
    Return a list of created node ids.
    """

    nodes = []
    elapsed_times = pandas.Series(dtype="float64")
    tps = pandas.Series(dtype="float64")
    bytes_received = pandas.Series(dtype="float64")
    error_count = 0
    node_text = TEXTS_APPENDER["small"]

    start = time.time_ns()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        results = [executor.submit(create_node, hierarchy_id, idx, node_text=node_text) for idx in range(size)]
        for future in concurrent.futures.as_completed(results):
            try:
                node_id, response_status, tps_per_thread, elapsed_ms, response_bytes = future.result()
                nodes.append(node_id)

                elapsed_times = elapsed_times.append(elapsed_ms, ignore_index=True)
                tps = tps.append(tps_per_thread, ignore_index=True)
                bytes_received = bytes_received.append(response_bytes, ignore_index=True)

                if response_status not in (200, 201):
                    error_count += 1

            except Exception as e:
                detail_logger.error(f"Creating node generated an exception: {e}")
            else:
                detail_logger.debug(f"Created a node; node id: {node_id}")
    finish = time.time_ns()
    elapsed_sec = (finish - start) / 1000000000
    detail_logger.info(f"Created a total of {size} nodes (with {workers} threads) for the hierarchy {hierarchy_id} in {str(round(elapsed_sec, 2))} seconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_CreateNode",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=workers,
                              transactionCount=size,
                              transactionsPerSecond=round(tps.mean() * workers, 2),
                              responseTimeMin=round(elapsed_times.min()),
                              responseTimeAverage=round(elapsed_times.mean()),
                              responseTimeMax=round(elapsed_times.max()),
                              responseTimeMedian=round(elapsed_times.median()),
                              responseTime90thPercentile=round(elapsed_times.quantile(0.9)),
                              responseTime95thPercentile=round(elapsed_times.quantile(0.95)),
                              apdex=apdex(elapsed_times),
                              byteSizeMin=round(bytes_received.min()),
                              byteSizeAverage=round(bytes_received.mean()),
                              byteSizeMax=round(bytes_received.max()),
                              errorsTotal=error_count,
                              errorsPercent=round(error_count / size, 2),
                              stepDuration=str(round(elapsed_sec))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)

    if latency:
        track_latency(
            elapsed_times, "Create Nodes Latency: pcm/hierarchies/<hierarchy_id>/nodes",
            "requests",
            "latency(ms)",
            "nodes"
        )

    return nodes


def create_product(idx: int, files_pool: cycle, product_text=""):
    """Create a product.

    The product with variations including the base products and their children products have tagged with the negative idx value,
    for exmaple, (-3) in "sku": "perf-sku--3_xxx"; the products without variations have tagged with non-negative idx value for
    exmaple, (5) in "sku": "perf-sku-5_xxx"
    """

    data = {
        "data": {
            "type": "product",
            "attributes": {
                "name": "perf product {}_{}".format(idx + 1, TAG),
                "description": "{} {}".format(TAG, product_text),
                "sku": "perf-sku-{}_{}".format(idx + 1, TAG),
                "slug": "perf-slug-{}_{}".format(idx + 1, TAG),
                "status": "live",
                "commodity_type": "physical"
            }
        }
    }
    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/products", headers=headers, json=data)
    finish = time.time_ns()

    r.raise_for_status()
    product_id = r.json()["data"]["id"]
    product_sku = r.json()["data"]["attributes"]["sku"]
    elapsed_ms = (finish - start) / 1000000

    # get response bytes
    response_bytes = len(r.content)
    # get reponse status
    response_status = r.status_code

    detail_logger.debug(f"Created product {product_id} SKU {product_sku} in {str(round(elapsed_ms, 2))} miliseconds")

    # Create multi-templates relationships to the current product
    if PRODUCTS_TEMPLATE_ENABLED:
        # multi templates to a single product according to our APIs
        create_products_templates_relationships(product_id)
        # then populate the entry values based on each template linked to the current product, and this is multi values per template per products according to our APIs
        for idx, template_slug in enumerate(flows):
            add_entries_to_products_template(template_slug, idx, product_id)

    # Create main image relationships to the current product
    main_image = {"type": "file"}
    main_image["id"] = next(files_pool)
    data = {}
    data["data"] = main_image

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/products/{product_id}/relationships/main_image", headers=headers, json=data)
    finish = time.time_ns()
    file_elapsed_ms = (finish - start) / 1000000
    detail_logger.debug(f"Associated the product {product_id} with main image in {str(round(file_elapsed_ms, 2))} miliseconds")

    # Create file relationships to the current product
    if NUM_FILES_PER_PRODUCT > 0:
        files = []
        for _ in range(NUM_FILES_PER_PRODUCT):
            file = {"type": "file"}
            file["id"] = next(files_pool)
            files.append(file)
        data = {}
        data["data"] = files

        start = time.time_ns()
        r = http.post(f"{SERVER}/pcm/products/{product_id}/relationships/files", headers=headers, json=data)
        finish = time.time_ns()
        file_elapsed_ms = (finish - start) / 1000000
        detail_logger.debug(f"Associated the product {product_id} with {NUM_FILES_PER_PRODUCT} files in {str(round(file_elapsed_ms, 2))} miliseconds")

    return product_id, product_sku, response_status, pandas.Series([1000 / elapsed_ms]), pandas.Series([elapsed_ms]), pandas.Series([response_bytes])


def populate_products(size: int, files_pool: cycle, workers=2, latency=False):
    """Populate the probduct either by Multi-threaded caller to create_product() to create the products via pcm product creation endpoint or build children products using pcm build endpoint.

    If it's first case, the number of workers thread is determined by the hosting machine and default is set to 2 threads.
    The outcome is to return a list of created products in a tuple pair (product_id, product_sku).
    """

    job_list = []
    products = []
    size_remaining_products = 0
    BUILD_JOB_SLEEP_TIME = 1        # wait time in seconds before issuing the next build children job
    product_text = TEXTS_APPENDER["medium"]

    # Build children variation products via pcm/build
    if NUM_BASE_PRODUCT:
        if size < NUM_BASE_PRODUCT * (NUM_OPTION ** NUM_VARIATION) + NUM_BASE_PRODUCT:
            detail_logger.error(f"Total number of products {TOTAL_PRODUCTS} has to be greater than the sum of children and base products \
                                {NUM_OPTION ** NUM_VARIATION} * {NUM_BASE_PRODUCT} + {NUM_BASE_PRODUCT} when building product variation. \
                                children products = NUM_OPTION ^ NUM_VARIATION * NUM_BASE_PRODUCT plus base products NUM_BASE_PRODUCT")
            sys.exit("The total number of given products does not satisfy the variation requirements!")

        # create variation first
        if NUM_VARIATION > 0 and NUM_OPTION > 0:
            extend_products_by_variations()

        # create base products and then go through base products to build children products
        for idx in range(NUM_BASE_PRODUCT):
            # create base products and the base products
            # the products with variation created in this way have tagged with the nagetive idx value in name and sku
            product_id, product_sku, *remaining = create_product(-2 - idx, files_pool, product_text=product_text)
            # Do NOT add base products to master product list as they can't be added to bundles and shouldn't connected to nodes
            # products.append((product_id, product_sku))
            detail_logger.info(f"Created a base product; product id: {product_id}; product sku: {product_sku}")

            # build product variations and options
            if NUM_VARIATION > 0 and NUM_OPTION > 0:
                # create product variation relationship to the base product
                for variation_id in variations:
                    create_products_variation_relationships(product_id, variation_id)
                # build the job for creating children products and add to job lists
                job_id, txn_summary = build_children_products(product_id)
                job_list.append((job_id, txn_summary, product_id))
                time.sleep(BUILD_JOB_SLEEP_TIME)

        # query the job status and get children products from the Mongo
        for job in job_list:
            job_id = None
            job_id, job_stats, base_product_id = job
            if job_id:
                query_children_proudcts_job_status(job_id, job_stats, interval=BUILD_JOB_SLEEP_TIME)

            # get children products list in a tuple of id and sku from the Mongo
            products += get_children_products(base_product_id)

        detail_logger.info(f"Total number of the children products was {len(products)} created by {NUM_BASE_PRODUCT} base products")

    # Get the count of the remaining products without variation. They will be done using APIs /pcm/products
    if NUM_BASE_PRODUCT:
        size_remaining_products = size - NUM_BUNDLES - NUM_BASE_PRODUCT - NUM_BASE_PRODUCT * (NUM_OPTION ** NUM_VARIATION)
    else:
        size_remaining_products = size - NUM_BUNDLES
    detail_logger.info(f"Total number remaining products to be created: {size_remaining_products}")

    # Create the products via pcm /pcm/products creation endpoint
    if size_remaining_products > 0:
        elapsed_times = pandas.Series(dtype="float64")
        tps = pandas.Series(dtype="float64")
        bytes_received = pandas.Series(dtype="float64")
        error_count = 0

        detail_logger.info("Creating products")

        start = time.time_ns()
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            results = [executor.submit(create_product, idx, files_pool, product_text=product_text) for idx in range(size_remaining_products)]
            for future in concurrent.futures.as_completed(results):
                try:
                    product_id, product_sku, response_status, tps_per_thread, elapsed_ms, response_bytes = future.result()
                    products.append((product_id, product_sku))

                    elapsed_times = elapsed_times.append(elapsed_ms, ignore_index=True)
                    tps = tps.append(tps_per_thread, ignore_index=True)
                    bytes_received = bytes_received.append(response_bytes, ignore_index=True)

                    if response_status not in (200, 201):
                        error_count += 1

                except Exception as e:
                    detail_logger.error(f"Creating a product generated an exception: {e}")
                else:
                    detail_logger.debug(f"Created a product; product id: {product_id}; product sku: {product_sku}")
        finish = time.time_ns()

        elapsed_sec = (finish - start) / 1000000000
        detail_logger.info(f"Created a total of {size} products (with {workers} threads) finished in {str(round(elapsed_sec, 2))} seconds")

        txn_summary = init_transaction_metric()
        update_transaction_metric(txn_summary,
                                  transactionName="UT_CreateProduct",
                                  timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                                  timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                                  virtualUsers=workers,
                                  transactionCount=size,
                                  transactionsPerSecond=round(tps.mean() * workers, 2),
                                  responseTimeMin=round(elapsed_times.min()),
                                  responseTimeAverage=round(elapsed_times.mean()),
                                  responseTimeMax=round(elapsed_times.max()),
                                  responseTimeMedian=round(elapsed_times.median()),
                                  responseTime90thPercentile=round(elapsed_times.quantile(0.9)),
                                  responseTime95thPercentile=round(elapsed_times.quantile(0.95)),
                                  apdex=apdex(elapsed_times),
                                  byteSizeMin=round(bytes_received.min()),
                                  byteSizeAverage=round(bytes_received.mean()),
                                  byteSizeMax=round(bytes_received.max()),
                                  errorsTotal=error_count,
                                  errorsPercent=round(error_count / size, 2),
                                  stepDuration=str(round(elapsed_sec))
                                  )
        log_transaction_metric(txn_summary)
        write_transaction_metabase(txn_summary)

        if latency:
            track_latency(
                elapsed_times, "Create Products Latency: pcm/products",
                "requests",
                "latency(ms)",
                "products"
            )

    random.shuffle(products)

    return products


def create_SKU_bundle(bundle: dict, files_pool: cycle, hierarchy_id: str, bundle_text=""):
    """Create SKU bundle consisting of N products."""

    components = {}
    iterator = 1
    for productID in bundle["productIDs"]:
        components["item" + str(iterator)] = {"max": 1, "min": 1, "name": "Item " + str(iterator), "options": [{"id": productID, "type": "product", "quantity": 1}]}
        iterator += 1

    # create a custom tag to identify the bundle prouduct with unique hierarchy
    tag = "{}_{}".format(hierarchy_id, TAG)
    data = {
        "data": {
            "type": "product",
            "attributes": {
                "name": "perf bundle {}_{}".format(bundle["index"] + 1, tag),
                "description": "{} {}".format(TAG, bundle_text),
                "sku": "perf-bundle-sku-{}_{}".format(bundle["index"] + 1, tag),
                "commodity_type": "physical",
                "status": "live",
                "components": components
            }
        }
    }

    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/products", headers=headers, json=data)
    finish = time.time_ns()
    elapsed_ms = (finish - start) / 1000000

    r.raise_for_status()
    bundle_id = r.json()["data"]["id"]
    bundle_sku = r.json()["data"]["attributes"]["sku"]
    # get response bytes
    response_bytes = len(r.content)
    # get reponse status
    response_status = r.status_code

    detail_logger.debug(f"Created a bundle with id {bundle_id} consisting of products {bundle}")

    # Create multi-templates relationships to the current bundle
    if PRODUCTS_TEMPLATE_ENABLED:
        # multi templates to a single bundle according to our APIs
        create_products_templates_relationships(bundle_id)
        # then populate the entry values based on each template linked to the current product, and this is multi values per template per products according to our APIs
        for idx, template_slug in enumerate(flows):
            add_entries_to_products_template(template_slug, idx, bundle_id)

    # Create file relationships to the current bundle
    if NUM_FILES_PER_PRODUCT > 0:
        files = []
        for _ in range(NUM_FILES_PER_PRODUCT):
            file = {"type": "file"}
            file["id"] = next(files_pool)
            files.append(file)
        data = {}
        data["data"] = files

        start = time.time_ns()
        r = http.post(f"{SERVER}/pcm/products/{bundle_id}/relationships/files", headers=headers, json=data)
        finish = time.time_ns()
        file_elapsed_ms = (finish - start) / 1000000
        detail_logger.debug(f"Associated the bundle {bundle_id} with {NUM_FILES_PER_PRODUCT} files in {str(round(file_elapsed_ms, 2))} miliseconds")

    return bundle_id, bundle_sku, response_status, pandas.Series([1000 / elapsed_ms]), pandas.Series([elapsed_ms]), pandas.Series([response_bytes])


def populate_bundles(size: int, products_list: list, files_pool: cycle, hierarchy_id: str, workers=2, latency=False):
    """Multi-threaded caller to create_SKU_bundle() to populate bundles built from a list of products."""

    bundles = []
    elapsed_times = pandas.Series(dtype="float64")
    tps = pandas.Series(dtype="float64")
    bytes_received = pandas.Series(dtype="float64")
    error_count = 0
    bundle_text = TEXTS_APPENDER["medium"]

    # Build a list of bundles to be created each consisting of N random product ID's
    for idx in range(NUM_BUNDLES):
        productIDs = []
        for i in range(NUM_PRODUCTS_PER_BUNDLE):
            productIDs.append(random.choice(products_list)[0])

        bundles.append({"index": idx, "productIDs": productIDs})

    start = time.time_ns()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        # first elememnt of product is product id, which is used to create bundles
        results = [executor.submit(create_SKU_bundle, bundle, files_pool, hierarchy_id, bundle_text=bundle_text) for bundle in bundles]
        for future in concurrent.futures.as_completed(results):
            try:
                bundle_id, bundle_sku, response_status, tps_per_thread, elapsed_ms, response_bytes = future.result()
                products_list.append((bundle_id, bundle_sku))

                elapsed_times = elapsed_times.append(elapsed_ms, ignore_index=True)
                tps = tps.append(tps_per_thread, ignore_index=True)
                bytes_received = bytes_received.append(response_bytes, ignore_index=True)

                if response_status not in (200, 201):
                    error_count += 1

            except Exception as e:
                detail_logger.error(f"Creating bundle {bundle_id} generated an exception: {e}")

    finish = time.time_ns()

    elapsed_sec = (finish - start) / 1000000000
    detail_logger.info(f"Populated a total of {len(bundles)} bundles (with {workers} threads) in {str(round(elapsed_sec, 2))} seconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_CreateBundles",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=workers,
                              transactionCount=len(bundles),
                              transactionsPerSecond=round(tps.mean() * workers, 2),
                              responseTimeMin=round(elapsed_times.min()),
                              responseTimeAverage=round(elapsed_times.mean()),
                              responseTimeMax=round(elapsed_times.max()),
                              responseTimeMedian=round(elapsed_times.median()),
                              responseTime90thPercentile=round(elapsed_times.quantile(0.9)),
                              responseTime95thPercentile=round(elapsed_times.quantile(0.95)),
                              apdex=apdex(elapsed_times),
                              byteSizeMin=round(bytes_received.min()),
                              byteSizeAverage=round(bytes_received.mean()),
                              byteSizeMax=round(bytes_received.max()),
                              errorsTotal=error_count,
                              errorsPercent=round(error_count / len(bundles), 2),
                              stepDuration=str(round(elapsed_sec))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)

    if latency:
        track_latency(
            elapsed_times, "Create Bundles Latency: pcm/products",
            "requests",
            "latency(ms)",
            "bundles"
        )
    return products_list


def create_pricebook():
    """Create a pricebook."""

    error_count = 0
    data = {
        "data": {
            "type": "pricebook",
            "attributes": {
                "name": "perf pricebook {}".format(TAG),
                "description": "Pricebook {} perflab test data {}".format(TAG, TEXTS_APPENDER["small"])
            }
        }
    }
    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/pricebooks", headers=headers, json=data)
    finish = time.time_ns()

    # get reponse status
    response_status = r.status_code
    if response_status not in (200, 201):
        error_count += 1
    r.raise_for_status()

    pricebook_id = r.json()["data"]["id"]
    # get response bytes
    response_bytes = len(r.content)
    elapsed_ms = (finish - start) / 1000000
    detail_logger.info(f"Created a pricebook with id {pricebook_id} in {str(round(elapsed_ms, 2))} miliseconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_CreatePricebook",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=1,
                              transactionCount=1,
                              transactionsPerSecond=round(1000 / elapsed_ms, 2),
                              responseTimeMin=round(elapsed_ms),
                              responseTimeAverage=round(elapsed_ms),
                              responseTimeMax=round(elapsed_ms),
                              responseTimeMedian=round(elapsed_ms),
                              responseTime90thPercentile=round(elapsed_ms),
                              responseTime95thPercentile=round(elapsed_ms),
                              apdex=apdex(pandas.Series([elapsed_ms])),
                              byteSizeMin=round(response_bytes),
                              byteSizeAverage=round(response_bytes),
                              byteSizeMax=round(response_bytes),
                              errorsTotal=error_count,
                              errorsPercent=round(float(error_count), 2),
                              stepDuration=str(round(elapsed_ms / 1000))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)

    return pricebook_id


def create_product_price(pricebook_id: str, product_sku: str):
    """Create a price for the given product in the pricebook."""

    data = {
        "data": {
            "type": "product-price",
            "attributes": {
                # "product_id": product_id,
                "sku": product_sku,
                "currencies": {
                    "USD": {
                        "amount": random.randint(1, 10000),
                        "includes_tax": False
                    }
                }
            }
        }
    }

    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/pricebooks/{pricebook_id}/prices", headers=headers, json=data)
    finish = time.time_ns()
    elapsed_ms = (finish - start) / 1000000

    r.raise_for_status()
    price_id = r.json()["data"]["id"]
    # get response bytes
    response_bytes = len(r.content)
    # get reponse status
    response_status = r.status_code

    detail_logger.debug(f"Created a price with id {price_id} for a product sku {product_sku} in a pricebook {pricebook_id} in {str(round(elapsed_ms, 2))} miliseconds")

    return price_id, response_status, pandas.Series([1000 / elapsed_ms]), pandas.Series([elapsed_ms]), pandas.Series([response_bytes])


def popluate_pricebook(pricebook_id: str, products_list: list, workers=2, latency=False):
    """Multi-threaded caller to create_product_price() to populate the prices for a list of products in the pricebook."""

    elapsed_times = pandas.Series(dtype="float64")
    tps = pandas.Series(dtype="float64")
    bytes_received = pandas.Series(dtype="float64")
    error_count = 0

    detail_logger.info("Creating prices for every product")

    start = time.time_ns()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        # second elememnt of product is product sku, which is used to create product price
        results = [executor.submit(create_product_price, pricebook_id, product[1]) for product in products_list]
        for future in concurrent.futures.as_completed(results):
            try:
                price_id, response_status, tps_per_thread, elapsed_ms, response_bytes = future.result()

                elapsed_times = elapsed_times.append(elapsed_ms, ignore_index=True)
                tps = tps.append(tps_per_thread, ignore_index=True)
                bytes_received = bytes_received.append(response_bytes, ignore_index=True)

                if response_status not in (200, 201):
                    error_count += 1

            except Exception as e:
                detail_logger.error(f"Creating a price generated an exception: {e}")
            else:
                detail_logger.debug(f"Created a price; price id: {price_id}")
    finish = time.time_ns()

    elapsed_sec = (finish - start) / 1000000000
    detail_logger.info(f"Populated a total of {len(products_list)} product prices (with {workers} threads) for the pricebook {pricebook_id} in {str(round(elapsed_sec, 2))} seconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_CreatePrice",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=workers,
                              transactionCount=len(products_list),
                              transactionsPerSecond=round(tps.mean() * workers, 2),
                              responseTimeMin=round(elapsed_times.min()),
                              responseTimeAverage=round(elapsed_times.mean()),
                              responseTimeMax=round(elapsed_times.max()),
                              responseTimeMedian=round(elapsed_times.median()),
                              responseTime90thPercentile=round(elapsed_times.quantile(0.9)),
                              responseTime95thPercentile=round(elapsed_times.quantile(0.95)),
                              apdex=apdex(elapsed_times),
                              byteSizeMin=round(bytes_received.min()),
                              byteSizeAverage=round(bytes_received.mean()),
                              byteSizeMax=round(bytes_received.max()),
                              errorsTotal=error_count,
                              errorsPercent=round(error_count / len(products_list), 2),
                              stepDuration=str(round(elapsed_sec))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)

    if latency:
        track_latency(
            elapsed_times, "Create Products Prices Latency: pcm/pricebooks/<pricebook_id>/prices",
            "requests",
            "latency(ms)",
            "prices"
        )


def create_product_inventory(product_id: str):
    """Create inventory for the given product."""

    data = {
        "data": {
            "quantity": NUM_INVENTORY
        }
    }

    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/v2/inventories/{product_id}", headers=headers, json=data)
    finish = time.time_ns()
    elapsed_ms = (finish - start) / 1000000

    r.raise_for_status()
    # get response bytes
    response_bytes = len(r.content)
    # get reponse status
    response_status = r.status_code

    detail_logger.debug(f"Created a inventory quantity of {NUM_INVENTORY} for product {product_id} in {str(round(elapsed_ms, 2))} miliseconds")

    return product_id, response_status, pandas.Series([1000 / elapsed_ms]), pandas.Series([elapsed_ms]), pandas.Series([response_bytes])


def create_inventories(products_list: list, workers=2, latency=False):
    """Multi-threaded caller to create_product_inventory() to populate the inventories for a list of products."""

    elapsed_times = pandas.Series(dtype="float64")
    tps = pandas.Series(dtype="float64")
    bytes_received = pandas.Series(dtype="float64")
    error_count = 0

    detail_logger.info("Creating inventory for every product")

    start = time.time_ns()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        # first elememnt of product is product id, which is used to create product inventory
        results = [executor.submit(create_product_inventory, product[0]) for product in products_list]
        for future in concurrent.futures.as_completed(results):
            try:
                product_id, response_status, tps_per_thread, elapsed_ms, response_bytes = future.result()

                elapsed_times = elapsed_times.append(elapsed_ms, ignore_index=True)
                tps = tps.append(tps_per_thread, ignore_index=True)
                bytes_received = bytes_received.append(response_bytes, ignore_index=True)

                if response_status not in (200, 201):
                    error_count += 1

            except Exception as e:
                detail_logger.error(f"Creating inventory for product_id {product_id} generated an exception: {e}")
            else:
                detail_logger.debug(f"Created inventory for product_id: {product_id}")

    finish = time.time_ns()

    elapsed_sec = (finish - start) / 1000000000
    detail_logger.info(f"Populated a total of {len(products_list)} product inventories (with {workers} threads) in {str(round(elapsed_sec, 2))} seconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_CreateInventory",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=workers,
                              transactionCount=len(products_list),
                              transactionsPerSecond=round(tps.mean() * workers, 2),
                              responseTimeMin=round(elapsed_times.min()),
                              responseTimeAverage=round(elapsed_times.mean()),
                              responseTimeMax=round(elapsed_times.max()),
                              responseTimeMedian=round(elapsed_times.median()),
                              responseTime90thPercentile=round(elapsed_times.quantile(0.9)),
                              responseTime95thPercentile=round(elapsed_times.quantile(0.95)),
                              apdex=apdex(elapsed_times),
                              byteSizeMin=round(bytes_received.min()),
                              byteSizeAverage=round(bytes_received.mean()),
                              byteSizeMax=round(bytes_received.max()),
                              errorsTotal=error_count,
                              errorsPercent=round(error_count / len(products_list), 2),
                              stepDuration=str(round(elapsed_sec))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)

    if latency:
        track_latency(
            elapsed_times, "Create Products Inventory Latency: v2/inventories/<product_id>",
            "requests",
            "latency(ms)",
            "inventories"
        )


def create_catalog(hierarchies: [], pricebook_id: str):
    """Create a new catalog."""

    hierarchy_ids = []
    for hierarchy in hierarchies:
        hierarchy_ids.append(hierarchy["id"])

    error_count = 0
    data = {
        "data": {
            "type": "catalog",
            "attributes": {
                "name": "perf catalog {}".format(TAG),
                "hierarchy_ids": hierarchy_ids,
                "pricebook_id": pricebook_id,
                "description": "Catalog {} perflab test data".format(TAG)
            }
        }
    }
    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/catalogs", headers=headers, json=data)
    finish = time.time_ns()

    # get reponse status
    response_status = r.status_code
    if response_status not in (200, 201):
        error_count += 1
    r.raise_for_status()

    catalog_id = r.json()["data"]["id"]
    # get response bytes
    response_bytes = len(r.content)
    elapsed_ms = (finish - start) / 1000000
    detail_logger.info(f"Created a catalog; catalog id: {catalog_id}; contains the pricebook id: {pricebook_id} and hierachy ids: {hierarchy_ids} in {str(round(elapsed_ms, 2))} miliseconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_CreateCatalog",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=1,
                              transactionCount=1,
                              transactionsPerSecond=round(1000 / elapsed_ms, 2),
                              responseTimeMin=round(elapsed_ms),
                              responseTimeAverage=round(elapsed_ms),
                              responseTimeMax=round(elapsed_ms),
                              responseTimeMedian=round(elapsed_ms),
                              responseTime90thPercentile=round(elapsed_ms),
                              responseTime95thPercentile=round(elapsed_ms),
                              apdex=apdex(pandas.Series([elapsed_ms])),
                              byteSizeMin=round(response_bytes),
                              byteSizeAverage=round(response_bytes),
                              byteSizeMax=round(response_bytes),
                              errorsTotal=error_count,
                              errorsPercent=round(float(error_count), 2),
                              stepDuration=str(round(elapsed_ms / 1000))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)

    return catalog_id


def release_catalog(catalog_id: str):
    """Release(or publish) a catalog."""

    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    detail_logger.info(f"Releasing a catalog; catalog id: {catalog_id}; at {datetime.now()}")
    r = requests.post(f"{SERVER}/pcm/catalogs/{catalog_id}/releases", headers=headers)

    finish = time.time_ns()
    release_id = None
    error_count = 0

    if r.status_code == 201:
        release_id = r.json()["data"]["id"]
        elapsed_ms = (finish - start) / 1000000
        # get response bytes
        response_bytes = len(r.content)

        detail_logger.info(f"Released a catalog; catalog id: {catalog_id}; release id: {release_id} in {str(round(elapsed_ms, 2))} miliseconds; at {datetime.now()}")
    else:
        detail_logger.warning(f"Getting HTTP {r.status_code} status when publishing the catalog with catalog id: {catalog_id}")
        error_count += 1

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_PublishCatalog",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=1,
                              transactionCount=1,
                              apdex=1.00,         # default apdex rule exampted for publishing catalog since it's long running asynchronous transaction
                              byteSizeMin=round(response_bytes),
                              byteSizeAverage=round(response_bytes),
                              byteSizeMax=round(response_bytes),
                              errorsTotal=error_count,
                              errorsPercent=round(float(error_count), 2)
                              )

    return release_id, txn_summary


def query_release_catalog_status(catalog_id: str, release_id: str, txn_summary: dict):
    """Check the release job status."""

    access_token = validate_token()
    headers = get_headers(access_token)

    start_time = None
    end_time = None

    while True:
        detail_logger.info(f"catalog id: {catalog_id}; release id: {release_id} publishing is still in progress...")
        # sleep 60 seconds and poke the release status again
        time.sleep(60)

        access_token = validate_token()
        headers = get_headers(access_token)
        r = http.get(f"{SERVER}/pcm/catalogs/{catalog_id}/releases/{release_id}", headers=headers)
        r.raise_for_status()
        status = r.json()["data"]["meta"]["release_status"]

        if status == "PUBLISHED":
            end_time = r.json()["data"]["attributes"]["published_at"]
            start_time = r.json()["data"]["meta"]["started_at"]
            break

    start = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%fZ')
    end = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S.%fZ')
    publish_time = (end - start).total_seconds()

    detail_logger.info(f"catalog id: {catalog_id}; release id: {release_id} has been published; published time took {str(publish_time)} seconds")

    # update publish time with asynchronous transaction time
    update_transaction_metric(txn_summary,
                              transactionsPerSecond=round(1 / publish_time, 2),
                              responseTimeMin=round(publish_time * 1000),
                              responseTimeAverage=round(publish_time * 1000),
                              responseTimeMax=round(publish_time * 1000),
                              responseTimeMedian=round(publish_time * 1000),
                              responseTime90thPercentile=round(publish_time * 1000),
                              responseTime95thPercentile=round(publish_time * 1000),
                              stepDuration=str(round(publish_time))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)


def get_db_stats(tag: str, db: pymongo.database.Database, col: str):
    """Get counts for given collections based on the filter tag from the given db."""

    collections = db[col]
    count = 0
    if col == "nodeProducts":
        count = collections.count_documents({"hierarchies": {"$in": [tag]}})
    elif col in ("prices", "projection_prices"):
        result = collections.aggregate([{"$match": {"sku": {"$regex": tag}}}, {"$count": "results"}], allowDiskUse=True)
        count = list(result)[0]["results"]
    else:
        result = collections.aggregate([{"$match": {"description": {"$regex": tag}}}, {"$count": "results"}], allowDiskUse=True)
        count = list(result)[0]["results"]

    return count


def validate_catalog_after_release(db: pymongo.database.Database):
    """Simple validation for a released/published catalog.

    Check if the db counts are matched between projection collections and snapshots collections.
    """

    start = datetime.now()
    detail_logger.info('\n')
    detail_logger.info(f"------------ Start validating a published catalog at {start} ------------")

    while True:
        # get nodes projection and snapshots collections
        nodes_cnt_projectdb = get_db_stats(f"{TAG} perflab test data", db, "projection_nodes")
        nodes_cnt_snapdb = get_db_stats(f"{TAG} perflab test data", db, "nodeSnapshots")

        # get prodcuts projection and snapshots collections
        products_cnt_projectdb = get_db_stats(TAG, db, "projection_products")
        products_cnt_snapdb = get_db_stats(TAG, db, "productSnapshots")

        if not nodes_cnt_projectdb:
            print(f"{nodes_cnt_projectdb}")
            detail_logger.error("Something wrent wrong! There are no nodes in projection db to publish. Check if Catalog-View has consumed all the events from PIM!")
            # continue

        elif not products_cnt_projectdb:
            detail_logger.error("Something wrent wrong! There are no products in projection db to publish. Check if Catalog-View has consumed all the events from PIM!")
            # continue

        else:
            if nodes_cnt_snapdb < nodes_cnt_projectdb:
                complete_pct = (nodes_cnt_snapdb / nodes_cnt_projectdb) * 100
                detail_logger.info(f"Total of nodes {nodes_cnt_projectdb} to be published, {nodes_cnt_snapdb} nodes has been published, {round(complete_pct, 2)}% of nodes completed")
            if products_cnt_snapdb < products_cnt_projectdb:
                complete_pct = (products_cnt_snapdb / products_cnt_projectdb) * 100
                detail_logger.info(f"Total of products {products_cnt_projectdb} to be published, {products_cnt_snapdb} products has been published, {round(complete_pct, 2)}% of products completed")
            else:
                end = datetime.now()
                length = (end - start).total_seconds()
                detail_logger.info(f"Catalog publishing is completed at {end}, took {length} seconds")
                break
        # sleep for some time to check again
        time.sleep(0.5)


def validate_rabbitmq_before_release(rabbitmq_config: dict, rabbitmq_queue: str):
    """ Simple validation piror to publishing a catalog.

    Check if the Rabbit MQ events has been consumed by Catalog-view prior to publishing a catalog.
    This is needed because publishing a catalog before Catalog-view consumes all the events from PIM and Pricebook would result an incompleted catalog in Catalog-view.
    """

    host = rabbitmq_config.get("host")
    port = rabbitmq_config.get("port")
    virtual_host = rabbitmq_config.get("virtual_host")
    user = rabbitmq_config.get("user")
    password = rabbitmq_config.get("password")

    start = datetime.now()
    detail_logger.info('\n')
    detail_logger.info(f"------------ Start validating the rabbitmq events prior to publishing the catalog at {start} ------------")

    for _ in range(3):
        idle = None
        # keep poking the status when the given rabbitmq queue is in traffic
        while not idle:
            r = requests.get(f"https://{host}:{port}/api/queues/{virtual_host}/{rabbitmq_queue}", auth=(user, password))
            r.raise_for_status()
            idle = r.json().get("idle_since")
            msg_count = r.json().get("messages")
            if not idle:
                detail_logger.info(f"RabbitMQ {rabbitmq_queue} is in traffic, has {msg_count} message")
            time.sleep(5)

    detail_logger.info(f"No more events in rabbitmq {rabbitmq_queue} queue at {datetime.now()}")


def validate_db_before_release(pim_db: pymongo.database.Database, cv_db: pymongo.database.Database, pb_db: pymongo.database.Database, hierarchies: []):
    """ Simple validation piror to publishing a catalog.

    Check if the Mongo records are matched between PIM, Pricebook and Catalog-view after Rabbit MQ events consumed by Catalog-view prior to publishing a catalog.
    This is needed because publishing a catalog before Catalog-view consumes all the events from PIM and Pricebook would result an incompleted catalog in Catalog-view.
    """

    start = datetime.now()
    detail_logger.info('\n')
    detail_logger.info(f"------------ Start validating all the Mongo recrods prior to publishing the catalog at {start} ------------")

    while True:
        # get prodcuts from PIM products and Catalog-view products projection collections
        products_cnt_pimdb = get_db_stats(TAG, pim_db, "products")
        products_cnt_projectdb = get_db_stats(TAG, cv_db, "projection_products")

        # get price from Pricebooks prices and Catalog-view prices projection collections
        prices_cnt_pricebookdb = get_db_stats(TAG, pb_db, "prices")
        # prices_cnt_projectdb = get_db_stats(TAG, cv_db, "projection_prices")

        # for hierarchy in hierarchies:
        #   get node and products from Catalog-view nodeProducts collections
        #   node_products_cnt_cvdb = get_db_stats(hierarchy["id"], cv_db, "nodeProducts")

        if not products_cnt_pimdb:
            detail_logger.error("Something wrent wrong! There are no products in PIM. Check if products have been created in PIM!")
            # continue

        elif not prices_cnt_pricebookdb:
            detail_logger.error("Something wrent wrong! There are no prices in Pricebooks. Check if prices have been created in Pricebooks!")
            # continue

        else:
            if products_cnt_projectdb < products_cnt_pimdb:
                complete_pct = (products_cnt_projectdb / products_cnt_pimdb) * 100
                detail_logger.info(f"Total of products {products_cnt_pimdb} in PIM, {products_cnt_projectdb} products got into Catalog-view projection, {round(complete_pct, 2)}% of products completed")
            # products prices was merged into products together stored in projection_products due to MT-7278 and  projections_prices is no longer used
            # if prices_cnt_projectdb != prices_cnt_pricebookdb:
            #     complete_pct = (prices_cnt_projectdb / prices_cnt_pricebookdb) * 100
            #     detail_logger.info(f"Total of prices {prices_cnt_pricebookdb} in Pricebooks, {prices_cnt_projectdb} prices got into Catalog-view projection, {round(complete_pct, 2)}% of prices completed")
            # if node_products_cnt_cvdb != products_cnt_pimdb:
            #     complete_pct = (node_products_cnt_cvdb / products_cnt_pimdb) * 100
            #     detail_logger.info(f"Total of products {products_cnt_pimdb} in PIM, {node_products_cnt_cvdb} products got into Catalog-view nodeProducts, {round(complete_pct, 2)}% of products completed")
            else:
                end = datetime.now()
                length = int((end - start).total_seconds())
                detail_logger.info(f"All of {products_cnt_pimdb} products in PIM, {prices_cnt_pricebookdb} prices in Pricebook have got into Catalog-view Projection db at {end}, took {length} seconds")
                break
        # sleep for some time to check again
        time.sleep(5)


def output_rabbitmq_stats(rabbitmq_config: dict, rabbitmq_queue: str):
    """Log the RabbitMQ stats."""

    host = rabbitmq_config.get("host")
    port = rabbitmq_config.get("port")
    virtual_host = rabbitmq_config.get("virtual_host")
    user = rabbitmq_config.get("user")
    password = rabbitmq_config.get("password")

    # sleep for 30 seconds and wait for traffic build up in rabbitmq
    time.sleep(30)
    for _ in range(3):
        idle = None
        # keep poking the status when the given rabbitmq queue is in traffic
        while not idle:
            r = requests.get(f"https://{host}:{port}/api/queues/{virtual_host}/{rabbitmq_queue}", auth=(user, password))
            r.raise_for_status()
            idle = r.json().get("idle_since")
            msg_count = r.json().get("messages")
            msg_publish_rate = r.json().get("message_stats").get("publish_details").get("rate")
            msg_consumer_ack_rate = r.json().get("message_stats").get("ack_details").get("rate")
            msg_deliver_ack_rate = r.json().get("message_stats").get("deliver_details").get("rate")
            if not idle:
                detail_logger.info(f"[RabbitMQ]: {msg_count} message, {msg_publish_rate} publish rate, {msg_deliver_ack_rate} deliver rate, {msg_consumer_ack_rate} consumer ack rate")
            # check every 5 seconds when there's continuous traffic
            time.sleep(5)
        detail_logger.info(f"[RabbitMQ]: {msg_count} message, {msg_publish_rate} publish rate, {msg_deliver_ack_rate} deliver rate, {msg_consumer_ack_rate} consumer ack rate")


def create_flow_feild(flow_id: str, slug: str, name: str, description: str):
    """Create a flow feild."""

    access_token = validate_token()
    headers = get_headers(access_token)

    try:
        data = {
            "data": {
                "type": "field",
                "field_type": "string",
                "slug": slug,
                "name": name,
                "description": description + TEXTS_APPENDER["small"],
                "required": False,
                "unique": False,
                "enabled": True,
                "order": 1,
                "omit_null": False,
                "relationships": {
                    "flow": {
                        "data": {
                            "type": "flow",
                            "id": flow_id
                        }
                    }
                }
            }
        }

        start = time.time_ns()
        r = http.post(f"{SERVER}/v2/fields", headers=headers, json=data)
        finish = time.time_ns()
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.status_code == 400:
            error_message = r.json().get("errors")
            detail_logger.info(f"HTTP error code {r.status_code}: {error_message}. Skip creating the flows feild!")
        else:
            detail_logger.info(f"HTTP error occurred when creating the flows {slug}: {e}!")
    else:
        field_id = r.json()["data"]["id"]
        field_slug = r.json()["data"]["slug"]
        elapsed_ms = (finish - start) / 1000000
        detail_logger.info(f"Created a field id: {str(field_id)}; feild slug: {str(field_slug)} for flow id: {flow_id} in {str(round(elapsed_ms, 2))} miliseconds; at {datetime.now()}")


def create_flow(slug: str, name: str, description: str):
    """Create a flow by existing a core resource."""

    access_token = validate_token()
    headers = get_headers(access_token)

    try:
        flow = {
            "data": {
                "type": "flow",
                "name": name,
                "slug": slug,
                "description": description + TEXTS_APPENDER["small"],
                "enabled": True
            }
        }

        start = time.time_ns()
        r = http.post(f"{SERVER}/v2/flows", headers=headers, json=flow)
        finish = time.time_ns()
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # When a flows already exits
        if r.status_code == 422:
            error_message = r.json().get("errors")
            detail_logger.info(f"HTTP error code {r.status_code}: {error_message}. Skip creating the flows!")
            raise requests.exceptions.HTTPError('422 Unprocessable Entity')
        else:
            detail_logger.info(f"HTTP error occurred when creating the flows {slug}: {e}!")
    else:
        flow_id = r.json()["data"]["id"]
        flows[slug] = flow_id
        elapsed_ms = (finish - start) / 1000000
        detail_logger.info(f"Created a flow; flow id: {flow_id}; flow slug: {str(slug)} in {str(round(elapsed_ms, 2))} miliseconds; at {datetime.now()}")


def create_products_templates_relationships(product_id: str):
    """Create the flows templates relationships with the products. This is multi templates per product call."""

    templates = []
    for template_id in flows.values():
        template = {"type": "template"}
        template["id"] = template_id
        templates.append(template)
    data = {}
    data["data"] = templates

    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/products/{product_id}/relationships/templates", headers=headers, json=data)
    finish = time.time_ns()

    r.raise_for_status()
    elapsed_ms = (finish - start) / 1000000
    detail_logger.debug(f"Associated ({len(flows)}) templates to product id {product_id} in {str(round(elapsed_ms, 2))} miliseconds; at {datetime.now()}")


def add_entries_to_products_template(template_slug: str, idx_template: int, product_id: str):
    """Add the entries values to the template that is assocated with the product. This is a per template per product call."""

    access_token = validate_token()
    headers = get_headers(access_token)

    data = {}
    entries = {"type": "entry", "id": product_id}
    for idx_field in range(NUM_FLOW_FIELD):
        entry = f"field_{TAG}-{str(idx_template)}-{str(idx_field)}"
        entries[entry] = f"{TAG} {TEXTS_APPENDER['small']}"
    data["data"] = entries

    start = time.time_ns()
    r = http.post(f"{SERVER}/v2/flows/{template_slug}/entries", headers=headers, json=data)
    finish = time.time_ns()

    r.raise_for_status()
    template_elapsed_ms = (finish - start) / 1000000
    detail_logger.debug(f"Added ({NUM_FLOW_FIELD}) entry values to the template slug {template_slug} associated with the product id {product_id} in {str(round(template_elapsed_ms, 2))} miliseconds; at {datetime.now()}")


def extend_products_by_templates():
    """Extend the PCM products by the templates."""

    for idx_template in range(NUM_TEMPLATE):
        template_slug = f"products(performance_{TAG}-{str(idx_template)})"
        create_flow(template_slug, template_slug.upper(), "Extends the default product object with custom fields in PCM ")

        for idx_field in range(NUM_FLOW_FIELD):
            field_slug = f"field_{TAG}-{str(idx_template)}-{str(idx_field)}"
            create_flow_feild(flows[template_slug], field_slug, field_slug.upper(), "PCM Perf feilds ")


def create_promotion_codes(promo_name: str, promo_id: str):
    """Create the promotion codes given the promotion name and id"""

    access_token = validate_token()
    headers = get_headers(access_token)

    codes = []
    for x in range(NUM_PROMOTION_CODE):
        codes.append({"code": promo_name + "_" + str(x)})

    data = {
        "data": {
            "type": "promotion_codes",
            "codes": codes
        }
    }

    start = time.time_ns()
    r = http.post(f"{SERVER}/v2/promotions/{promo_id}/codes", headers=headers, json=data)
    finish = time.time_ns()

    r.raise_for_status()
    elapsed_ms = (finish - start) / 1000000
    detail_logger.debug(f"Created {len(codes)} codes for Promotion name: {promo_name} in {str(round(elapsed_ms, 2))} miliseconds; at {datetime.now()}")


def create_promotions(catalog_id, target_catalogs=False):
    """Create the promotions.

    Promotions work at store level. It would skip the promotion creations if they already created before.
    By default, the promotion will not get attached to any catalogs.
    """

    access_token = validate_token()
    headers = get_headers(access_token)

    # Get a list of existing promotion names in the store
    promotions_name_list = []
    r = http.get(f"{SERVER}/v2/promotions?page[offset]=0&page[limit]=100", headers=headers)
    r.raise_for_status()
    current = r.json()["links"]["current"]
    next = r.json()["links"]["next"]
    last = r.json()["links"]["last"]
    promotions_list = r.json()["data"]
    promotions_name_list += [item.get("name") for item in promotions_list]
    while (current != last):
        current = next
        r = http.get(current, headers=headers)
        promotions_list = r.json()["data"]
        promotions_name_list += [item.get("name") for item in promotions_list]
        current = r.json()["links"]["current"]
        next = r.json()["links"]["next"]

    for x in range(NUM_PROMOTION):
        name = "PERFPROM_" + str(x)

        # promotion does not exist so create it
        if name not in promotions_name_list:
            percentage = random.randint(5, 60)

            promotion = None
            promotion = {
                "data": {
                    "type": "promotion",
                    "enabled": True,
                    "start": "2021-01-01",
                    "end": "2099-01-01",
                    "promotion_type": "percent_discount",
                    "name": "PERFPROM_" + str(x),
                    "description": "Percent Discount Promotion " + "PERFPROM_" + str(x),
                    "schema": {
                        "currencies": [
                            {
                                "currency": "GBP",
                                "percentage": percentage
                            },
                            {
                                "currency": "USD",
                                "percentage": percentage
                            }
                        ]
                    }
                }
            }

            if target_catalogs:
                promotion = {
                    "data": {
                        "type": "promotion",
                        "enabled": True,
                        "start": "2021-01-01",
                        "end": "2099-01-01",
                        "promotion_type": "percent_discount",
                        "name": "PERFPROM_" + str(x),
                        "description": "Percent Discount Promotion " + "PERFPROM_" + str(x),
                        "schema": {
                            "currencies": [
                                {
                                    "currency": "GBP",
                                    "percentage": percentage
                                },
                                {
                                    "currency": "USD",
                                    "percentage": percentage
                                }
                            ],
                            "target_catalogs": [catalog_id]
                        }
                    }
                }

            start = time.time_ns()
            r = http.post(f"{SERVER}/v2/promotions", headers=headers, json=promotion)
            finish = time.time_ns()

            r.raise_for_status()

            promotion_id = r.json()["data"]["id"]
            promotion_name = r.json()["data"]["name"]
            elapsed_ms = (finish - start) / 1000000
            detail_logger.info(f"Created Promotion id: {promotion_id}, promotion name: {promotion_name} in {str(round(elapsed_ms, 2))} miliseconds; at {datetime.now()}")

            # create promotion codes for a specific promotion
            create_promotion_codes(promotion_name, promotion_id)
        else:
            detail_logger.info(f"Promotions {name} already existed and skipped the creations; at {datetime.now()}")


def create_file(idx: int):
    """Creart a file in PCM."""

    access_token = validate_token()
    headers = get_headers(access_token)

    # removed the content type as it will be set by the request with multipart/form-data automatically as in the header
    if "Content-Type" in headers:
        del headers["Content-Type"]

    try:
        with open("tests/resources/data/files/main.jpg", "rb") as f:
            files = [('file', ('perf-file-{}_{}.jpg'.format(idx + 1, TAG), f, 'image/jpeg'))]
            start = time.time_ns()
            r = http.post(f"{SERVER}/v2/files", headers=headers, files=files, data={"public": "false"})
            finish = time.time_ns()

            r.raise_for_status()
            image_id = r.json()["data"]["id"]
            elapsed_ms = (finish - start) / 1000000
            response_bytes = len(r.content)
            response_status = r.status_code
            detail_logger.debug(f"Created the file with ID: {image_id} in {str(round(elapsed_ms, 2))} miliseconds; at {datetime.now()}")
            return image_id, response_status, pandas.Series([1000 / elapsed_ms]), pandas.Series([elapsed_ms]), pandas.Series([response_bytes])

    except FileNotFoundError as e:
        detail_logger.error(f"The file main.jpg was not found: {e}")

    except Exception as e:
        detail_logger.error(f"Something went wrong when creating the main image file: {e}")
        raise


def populate_files(size: int, workers=2, latency=False):
    """Populate files by Multi-threaded call to create_file()

    The number of workers thread is determined by the hosting machine and default is set to 2 threads.
    Return a list of created file id's
    """

    files = []
    elapsed_times = pandas.Series(dtype="float64")
    tps = pandas.Series(dtype="float64")
    bytes_received = pandas.Series(dtype="float64")
    error_count = 0

    start = time.time_ns()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        results = [executor.submit(create_file, idx) for idx in range(size)]
        for future in concurrent.futures.as_completed(results):
            try:
                file_id, response_status, tps_per_thread, elapsed_ms, response_bytes = future.result()
                files.append(file_id)

                elapsed_times = elapsed_times.append(elapsed_ms, ignore_index=True)
                tps = tps.append(tps_per_thread, ignore_index=True)
                bytes_received = bytes_received.append(response_bytes, ignore_index=True)

                if response_status not in (200, 201):
                    error_count += 1

            except Exception as e:
                detail_logger.error(f"Creating file {file_id} generated an exception: {e}")

    finish = time.time_ns()

    elapsed_sec = (finish - start) / 1000000000
    detail_logger.info(f"Populated a total of {len(files)} files (with {workers} threads) in {str(round(elapsed_sec, 2))} seconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_CreateFiles",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=workers,
                              transactionCount=size,
                              transactionsPerSecond=round(tps.mean() * workers, 2),
                              responseTimeMin=round(elapsed_times.min()),
                              responseTimeAverage=round(elapsed_times.mean()),
                              responseTimeMax=round(elapsed_times.max()),
                              responseTimeMedian=round(elapsed_times.median()),
                              responseTime90thPercentile=round(elapsed_times.quantile(0.9)),
                              responseTime95thPercentile=round(elapsed_times.quantile(0.95)),
                              apdex=apdex(elapsed_times),
                              byteSizeMin=round(bytes_received.min()),
                              byteSizeAverage=round(bytes_received.mean()),
                              byteSizeMax=round(bytes_received.max()),
                              errorsTotal=error_count,
                              errorsPercent=round(error_count / size, 2),
                              stepDuration=str(round(elapsed_sec))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)

    if latency:
        track_latency(
            elapsed_times, "Create Files Latency: v2/files",
            "requests",
            "latency(ms)",
            "files"
        )

    random.shuffle(files)
    return files


def create_context_rule(catalog_id: str):
    """Create a catalog context rule to mark the catalog."""

    error_count = 0
    channel_list = []
    channel_list.append(str(CATALOG_RULE_NAME))
    data = {
        "data": {
            "type": "catalog_rule",
            "attributes": {
                "name": "Perf context rule created by automation {}".format(TAG),
                "description": "Perf context {}".format(TAG),
                "catalog_id": catalog_id,
                "channels": channel_list
            }
        }
    }
    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/catalogs/rules", headers=headers, json=data)
    finish = time.time_ns()

    # get reponse status
    response_status = r.status_code
    if response_status not in (200, 201):
        error_count += 1
    r.raise_for_status()

    rule_id = r.json()["data"]["id"]
    # get response bytes
    response_bytes = len(r.content)
    elapsed_ms = (finish - start) / 1000000
    detail_logger.info(f"Created a rule; rule_id: {rule_id} in {str(round(elapsed_ms, 2))} miliseconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_CreateRules",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=1,
                              transactionCount=1,
                              transactionsPerSecond=round(1000 / elapsed_ms, 2),
                              responseTimeMin=round(elapsed_ms),
                              responseTimeAverage=round(elapsed_ms),
                              responseTimeMax=round(elapsed_ms),
                              responseTimeMedian=round(elapsed_ms),
                              responseTime90thPercentile=round(elapsed_ms),
                              responseTime95thPercentile=round(elapsed_ms),
                              apdex=apdex(pandas.Series([elapsed_ms])),
                              byteSizeMin=round(response_bytes),
                              byteSizeAverage=round(response_bytes),
                              byteSizeMax=round(response_bytes),
                              errorsTotal=error_count,
                              errorsPercent=round(float(error_count), 2),
                              stepDuration=str(round(elapsed_ms / 1000))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)

    return rule_id


def create_products_variation(variation_name: str):
    """Create a product variation."""

    error_count = 0
    data = {
        "data": {
            "type": "product-variation",
            "attributes": {
                "name": f"Perf{TAG}_{variation_name} {TEXTS_APPENDER['xxsmall']}"
            }
        }
    }
    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/variations", headers=headers, json=data)
    finish = time.time_ns()

    # get reponse status
    response_status = r.status_code
    if response_status not in (200, 201):
        error_count += 1
    r.raise_for_status()

    variation_id = r.json()["data"]["id"]
    # get response bytes
    response_bytes = len(r.content)
    elapsed_ms = (finish - start) / 1000000
    detail_logger.info(f"Created a variation; variation_id: {variation_id} in {str(round(elapsed_ms, 2))} miliseconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_CreateVariation",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=1,
                              transactionCount=1,
                              transactionsPerSecond=round(1000 / elapsed_ms, 2),
                              responseTimeMin=round(elapsed_ms),
                              responseTimeAverage=round(elapsed_ms),
                              responseTimeMax=round(elapsed_ms),
                              responseTimeMedian=round(elapsed_ms),
                              responseTime90thPercentile=round(elapsed_ms),
                              responseTime95thPercentile=round(elapsed_ms),
                              apdex=apdex(pandas.Series([elapsed_ms])),
                              byteSizeMin=round(response_bytes),
                              byteSizeAverage=round(response_bytes),
                              byteSizeMax=round(response_bytes),
                              errorsTotal=error_count,
                              errorsPercent=round(float(error_count), 2),
                              stepDuration=str(round(elapsed_ms / 1000))
                              )
    log_transaction_metric(txn_summary)
    # write_transaction_metabase(txn_summary)

    return variation_id


def create_products_option(option_name: str, option_description: str, variation_id: str):
    """Create a product variation option."""

    error_count = 0
    data = {
        "data": {
            "type": "product-variation-option",
            "attributes": {
                "name": option_name,
                "description": f"Perf{TAG}_{option_description} {TEXTS_APPENDER['xsmall']}"
            }
        }
    }
    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/variations/{variation_id}/options", headers=headers, json=data)
    finish = time.time_ns()

    # get reponse status
    response_status = r.status_code
    if response_status not in (200, 201):
        error_count += 1
    r.raise_for_status()

    option_id = r.json()["data"]["id"]
    # get response bytes
    response_bytes = len(r.content)
    elapsed_ms = (finish - start) / 1000000
    detail_logger.info(f"Created a variation option; option_id: {option_id} in {str(round(elapsed_ms, 2))} miliseconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_CreateOption",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=1,
                              transactionCount=1,
                              transactionsPerSecond=round(1000 / elapsed_ms, 2),
                              responseTimeMin=round(elapsed_ms),
                              responseTimeAverage=round(elapsed_ms),
                              responseTimeMax=round(elapsed_ms),
                              responseTimeMedian=round(elapsed_ms),
                              responseTime90thPercentile=round(elapsed_ms),
                              responseTime95thPercentile=round(elapsed_ms),
                              apdex=apdex(pandas.Series([elapsed_ms])),
                              byteSizeMin=round(response_bytes),
                              byteSizeAverage=round(response_bytes),
                              byteSizeMax=round(response_bytes),
                              errorsTotal=error_count,
                              errorsPercent=round(float(error_count), 2),
                              stepDuration=str(round(elapsed_ms / 1000))
                              )
    log_transaction_metric(txn_summary)
    # write_transaction_metabase(txn_summary)

    return option_id


def create_products_variation_relationships(base_product_id: str, variation_id: str):
    """Create a product variation relationship to the base product."""

    error_count = 0
    data = {
        "data": [
            {
                "type": "product-variation",
                "id": variation_id
            }
        ]
    }
    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    r = http.post(f"{SERVER}/pcm/products/{base_product_id}/relationships/variations", headers=headers, json=data)
    finish = time.time_ns()

    # get reponse status
    response_status = r.status_code
    if response_status not in (200, 201):
        error_count += 1
    r.raise_for_status()

    # get response bytes
    response_bytes = len(r.content)
    elapsed_ms = (finish - start) / 1000000
    detail_logger.info(f"Attached variation: {variation_id} to the base product: {base_product_id} in {str(round(elapsed_ms, 2))} miliseconds")

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_AttachVariation",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=1,
                              transactionCount=1,
                              transactionsPerSecond=round(1000 / elapsed_ms, 2),
                              responseTimeMin=round(elapsed_ms),
                              responseTimeAverage=round(elapsed_ms),
                              responseTimeMax=round(elapsed_ms),
                              responseTimeMedian=round(elapsed_ms),
                              responseTime90thPercentile=round(elapsed_ms),
                              responseTime95thPercentile=round(elapsed_ms),
                              apdex=apdex(pandas.Series([elapsed_ms])),
                              byteSizeMin=round(response_bytes),
                              byteSizeAverage=round(response_bytes),
                              byteSizeMax=round(response_bytes),
                              errorsTotal=error_count,
                              errorsPercent=round(float(error_count), 2),
                              stepDuration=str(round(elapsed_ms / 1000))
                              )
    log_transaction_metric(txn_summary)
    # write_transaction_metabase(txn_summary)


def build_children_products(base_product_id: str):
    """Build children products based on the base product. This triggers a build job."""

    access_token = validate_token()
    headers = get_headers(access_token)

    start = time.time_ns()
    detail_logger.info(f"Starting building children products based on base product: {base_product_id}; at {datetime.now()}")
    r = requests.post(f"{SERVER}/pcm/products/{base_product_id}/build", headers=headers)

    finish = time.time_ns()
    job_id = None
    error_count = 0

    if r.status_code == 201:
        job_id = r.json()["data"]["id"]
        elapsed_ms = (finish - start) / 1000000
        # get response bytes
        response_bytes = len(r.content)

        detail_logger.info(f"Building children products based on base product id: {base_product_id} in {str(round(elapsed_ms, 2))} miliseconds")
    else:
        detail_logger.warning(f"Getting HTTP {r.status_code} status when building children products based on base product: {base_product_id}")
        error_count += 1

    txn_summary = init_transaction_metric()
    update_transaction_metric(txn_summary,
                              transactionName="UT_BuildProductsJob",
                              timeStart=str(datetime.fromtimestamp(start / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              timeStop=str(datetime.fromtimestamp(finish / 1000000000).strftime('%Y-%m-%d %H:%M:%S')),
                              virtualUsers=1,
                              transactionCount=1,
                              apdex=1.00,         # default apdex rule exampted for publishing catalog since it's long running asynchronous transaction
                              byteSizeMin=round(response_bytes),
                              byteSizeAverage=round(response_bytes),
                              byteSizeMax=round(response_bytes),
                              errorsTotal=error_count,
                              errorsPercent=round(float(error_count), 2)
                              )

    return job_id, txn_summary


def query_children_proudcts_job_status(job_id: str, txn_summary: dict, interval=5):
    """Check the build products job status."""

    access_token = validate_token()
    headers = get_headers(access_token)

    start_time = None
    end_time = None
    job_time = 0

    while True:
        # sleep by given interval (in seconds) and poke the job status
        time.sleep(interval)

        r = http.get(f"{SERVER}/pcm/jobs/{job_id}", headers=headers)
        r.raise_for_status()
        status = r.json()["data"]["attributes"]["status"]
        detail_logger.info(f"Build children product job: {job_id} is still in progress...")

        if status == "success":
            start_time = r.json()["data"]["attributes"]["created_at"]
            end_time = r.json()["data"]["attributes"]["updated_at"]
            break
    try:
        if not start_time and not end_time:
            start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f %z %Z')
            end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S.%f %z %Z')
            job_time = (end - start).total_seconds()
            detail_logger.info(f"Build children product job: {job_id} has been completed; job took {str(job_time)} seconds")
    except Exception as e:
        detail_logger.error(f"Failed to get job start time {start_time} and end time {end_time} for building children product job: {job_id}: {e}")

    # update publish time with asynchronous transaction time
    # avoid divide zero error if job time takes less than a second
    if job_time < 1:
        job_time = 1
    update_transaction_metric(txn_summary,
                              transactionsPerSecond=round(1 / job_time, 2),
                              responseTimeMin=round(job_time * 1000),
                              responseTimeAverage=round(job_time * 1000),
                              responseTimeMax=round(job_time * 1000),
                              responseTimeMedian=round(job_time * 1000),
                              responseTime90thPercentile=round(job_time * 1000),
                              responseTime95thPercentile=round(job_time * 1000),
                              stepDuration=str(round(job_time))
                              )
    log_transaction_metric(txn_summary)
    write_transaction_metabase(txn_summary)


def get_children_products(parent_product_id: str):
    """Get all the children products from the build job given parent product id.

    Note: we can use PIM endpoint/children to get a list of children products but there is the overhead
    due to the pagination so let's get the list directly from the mongo collection in one go since we
    need to know the children prodcuts tuple of id and sku later.
    """

    client_pim = pymongo.MongoClient(MONGO_DNS_PIM)
    products_collection = client_pim["productManagement"]["products"]

    products_build = products_collection.find({"sku": {"$regex": f"perf-sku-.*{TAG}.*"}, "tenant": STORE_ID, "parent_id": parent_product_id}, allow_disk_use=True)

    tuple_product_list = [(product["_id"], product["sku"]) for product in products_build]
    detail_logger.info(f"Successfully built a total of {len(tuple_product_list)} children products at {datetime.now()} for the given base product {parent_product_id} \
                       vs. expected the number of children products {NUM_OPTION ** NUM_VARIATION} (= Options ^ Variations)")

    return tuple_product_list


def extend_products_by_variations():
    """Extend the PCM products by building children products via the product variations."""

    for variation_idx in range(NUM_VARIATION):
        variation_id = create_products_variation(f"VAR{variation_idx}")
        variations.append(variation_id)

        for options_idx in range(NUM_OPTION):
            create_products_option(f"VAR{variation_idx}OPT{options_idx}", "perf testing", variation_id)


def create_carts_flow():
    """Creat a core flow by extending the carts."""

    try:
        create_flow("carts", "carts", "Extending the carts resource")
    except requests.exceptions.HTTPError:
        detail_logger.info("Extending the Core flows slug carts already existed in the store. Skip creating the flows")
    else:
        for idx in range(NUM_CARTS_CORE_FLOW_FIELD):
            create_flow_feild(flows["carts"], f"carts_flows_feilds-{idx}", f"carts_flows_feilds-{idx}", f"FLows feilds {idx} extending the carts resource")


def main():

    detail_logger.info(f"Run tag: {TAG}")

    # run the rabbitmq stats output job in the background
    # [2022-05] temporally commit out
    # rabbitmq_config = dict(host=RABBITMQ_HOST, port=RABBITMQ_PORT, virtual_host=RABBITMQ_VIRTUAL_HOST, user=RABBITMQ_USER, password=RABBITMQ_PASSWORD)
    # rabbit_proc = Process(target=output_rabbitmq_stats, args=(rabbitmq_config, RABBITMQ_QUEUE))
    # rabbit_proc.start()

    # get the autentication token
    get_authorized_token()

    # extend pcm products using the flows templates
    if PRODUCTS_TEMPLATE_ENABLED:
        extend_products_by_templates()

    # create a hierarchies and nodes
    hierarchies = []
    for h in range(HIERARCHIES):
        hierarchy_dict = {}
        hierarchy_dict["id"] = create_hierarchy()
        node_ids = populate_nodes(hierarchy_dict["id"], get_num_nodes() - 1, workers=THREAD_NODE, latency=True)
        hierarchy_dict["tree"] = create_hierarchy_tree(hierarchy_dict["id"], node_ids)
        hierarchies.append(hierarchy_dict)

    files_list = populate_files(TOTAL_FILES, workers=THREAD_PRODUCT, latency=True)
    # use to iterate the files attaching to the products later
    files_pool = cycle(files_list)

    # there are two ways of creating products in current build-out implementation:
    # one way is through regular product creations endpoints and the other way is done using build children products endpoints.
    # - it will first create the products with variations if NUM_BASE_PRODUCT and Variations and Options were specificied.
    # - whatever the remaining products without any variations will be created via using regular product creation endpoint.
    # the return of this call would create a list of prodcts tuple containing a tuple pair of (product_id, product_sku) as some
    # serivces like Pricebook needs product_sku and other services like Inventories needs product id.
    products_list = populate_products(TOTAL_PRODUCTS, files_pool, workers=THREAD_PRODUCT, latency=True)

    # create sku bundles and add them to the product list if config is set to create them
    if NUM_BUNDLES:
        products_list = populate_bundles(NUM_BUNDLES, products_list, files_pool, hierarchies[0]["id"], workers=THREAD_BUNDLES, latency=True)

    # use to iterate the products attaching to the nodes later
    products_pool = cycle(products_list)

    # create a pricebook and populate the products prices for that pricebook
    pricebook_id = create_pricebook()
    popluate_pricebook(pricebook_id, products_list, workers=THREAD_PRICE, latency=True)

    # create inventory for every product if inventory is enabled
    if INVENTORY_ENABLED:
        create_inventories(products_list, workers=THREAD_INVENTORY, latency=True)

    # for each hierarchy attach products to nodes
    for hierarchy in hierarchies:
        # assume we do not attach the product to the hierarch node (e.g. root node)
        nodes_list = [hierarchy["tree"][node] for node in hierarchy["tree"].expand_tree(mode=Tree.ZIGZAG) if not hierarchy["tree"].get_node(node).is_root()]
        populate_products_in_node(hierarchy["id"], nodes_list, products_pool, workers=THREAD_PRODUCT2NODE, latency=True)

        # show and draw the tree of hierachy and nodes
        show(hierarchy["tree"], data_property="products")
        # draw(hierarchy_ds[h])

    # validate the catalog-view had consumed all the events from PIM and Pricebooks
    # [2022-05] temporally commit out
    # validate_rabbitmq_before_release(rabbitmq_config, RABBITMQ_QUEUE)
    detail_logger.info("------------ sleep 30 minutes ------------")
    time.sleep(1800)

    client_pim = pymongo.MongoClient(MONGO_DNS_PIM)
    client_cv = pymongo.MongoClient(MONGO_DNS_CATALOGVIEW)
    client_pb = pymongo.MongoClient(MONGO_DNS_PRICEBOOKS)
    # validate mongo projection as the result of consumming all rabbit events
    validate_db_before_release(client_pim.productManagement, client_cv.catalog_view, client_pb.pricebooks, hierarchies)
    client_pim.close()
    client_pb.close()

    # create a catalog
    catalog_id = create_catalog(hierarchies, pricebook_id)

    # release/publish a catalog and call to update the transaction metrics twice (ie. one for start and one for complete) as it's long running asynchronous
    release_id, txn_summary = release_catalog(catalog_id)
    query_release_catalog_status(catalog_id, release_id, txn_summary)

    # create a context rules for the publish catalog
    create_context_rule(catalog_id)

    # create promotions
    if NUM_PROMOTION:
        create_promotions(catalog_id, target_catalogs=False)

    # create core flows extending from the carts
    if CORE_CARTS_FLOW_ENABLED:
        create_carts_flow()

    # [2022-05] temporally commit out
    # rabbit_proc.join()

    # validate the released/published catalog
    validate_catalog_after_release(client_cv.catalog_view)
    client_cv.close()


main()