import json
import sys
import dateutil.parser
from html import HTML


class JobParser:
    # track # of jobs
    totalJobCount = 0

    def __init__(self, data, tag_name):
        # raw data reading from file in json format
        self.data = data
        # tag is application portfolio name
        self.tagName = tag_name
        # store the result after parsing the data (json)
        self.jobDictionary = {}
        JobParser.totalJobCount += 1

    @classmethod
    def get_job_count(cls):
        return cls.totalJobCount

    # get job in json raw format read in from file
    def get_job_data(self):
        return self.data

    # return job dictionary
    def get_job_dictionary(self):
        return self.jobDictionary

    def set_job_dictionary(self, key, value):
        jobDict = self.get_job_dictionary()
        jobDict[key] = value

    def parse(self):
        json = self.get_job_data()
        self.parse_request(json)
        self.parse_reply(json)
        self.parse_update(json)

    def parse_request(self, json):
        try:
            for item in json['results']['dmf']['ingest']:
                # There is only 1 item in request per ingest so it's safe here to loop through by key
                for key in item:
                    ingestTime = item[key][0]
        except:
            print("no Request")
        else:
            self.set_job_dictionary("ingestTime", ingestTime)

    def parse_reply(self, json):
        try:
            for item in json['results']['dmf']['reply']:
                # There is only 1 item in reply per ingest so it safe here to loop through by key
                for key in item:
                    replyAcceptTime = item[key][0]
                    replySentTime = item[key][1]
        except:
            print("no Reply")
        else:
            self.set_job_dictionary("replyTimeAccept", replyAcceptTime)
            self.set_job_dictionary("replyTimeSent", replySentTime)

    def parse_update(self, json):
        try:
            # There could be multiple actions (items) defined in workflow per ingest
            action_items = json['results']['dmf']['update']
        except:
            print("no Update")
        else:
            item_count = len(action_items)
            self.set_job_dictionary("actionCount", item_count)

            for index in range(item_count):
                action_index = '{}_{}'.format('actionName', index)
                task_set = action_items[index]
                self.set_job_dictionary(action_index, str(task_set.keys()[0]))
                # print str(task_set.keys()[0])

                try:
                    print task_set[self.get_job_dictionary()[action_name]].keys()
                    action_name = self.get_job_dictionary()[action_index]
                    #self.set_job_dictionary(action_name, )

                except:
                    print("no Action")








def generate_html(FLOW, INGEST_TIME, ACITION_BEGIN_TIME, ACITION_SUCCESS_TIME):
    html = HTML()
    html = html.html()

    head = html.head
    head.title('Performance Metrics')
    head.meta(content='text/html; charset=utf-8')
    head.link(rel='stylesheet', href='main.css', type='text/css')

    table = html.body.table()

    t_row1 = table.tr
    t_row1.th('Application Portfolio - ' + FLOW)
    t_row1.th('INGEST REQUEST')
    t_row1.th('EXECUTE_ACTION', colspan='3')
    t_row1.th('END TO END')

    t_row2 = table.tr
    t_row2.th('Job Name')
    t_row2.th('Request Time [UTC]')
    t_row2.th('Action Begin [UTC]')
    t_row2.th('Action Success [UTC]')
    t_row2.th('Action Processing Time')
    t_row2.th('Processing Time')

    # convert string to datetime
    dt_1 = dateutil.parser.parse(INGEST_TIME)
    dt_2 = dateutil.parser.parse(ACITION_BEGIN_TIME)
    dt_3 = dateutil.parser.parse(ACITION_SUCCESS_TIME)

    t_row3 = table.tr
    t_row3.td(JOB_NAME)
    # Ingest time from client - concert it (usually based on Eastern time to DMF timezone time (utc) and then chop the date prefix
    t_row3.td(dt_1.astimezone(dt_2.tzinfo).strftime('%H:%M:%S.%f'))
    t_row3.td(dt_2.strftime('%H:%M:%S.%f'))
    # t_row3.td(str(dt_3))
    t_row3.td(dt_3.strftime('%H:%M:%S.%f'))

    t_row3.td('{} {}'.format(str(dt_3 - dt_2), "| [" + str((dt_3 - dt_2).seconds) + "] secs"))

    # amazing - timedelta can do the difference by observing the time zone difference!
    # dt_1: 2018 - 10 - 03T18:55:31.955000 - 04:00
    # dt_3: 2018 - 10 - 03T22:59:16.886432 + 00:00
    t_row3.td('{} {}'.format(str(dt_3 - dt_1), "| [" + str((dt_3 - dt_1).seconds) + "] secs"))

    with open('performance.html', 'w') as f:
        f.writelines(html)


if __name__ == '__main__':
    tag = str((sys.argv[1]))

    #print(JobParser.totalJobCount)

    with open('json\\sample.json', 'r') as f:
        parser = JobParser(json.load(f), tag)
        parser.parse()

    #print(JobParser.get_job_count())
