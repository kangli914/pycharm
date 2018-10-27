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
        self.tag = tag_name
        # store the result after parsing the data (json)
        self.jobDictionary = {}
        JobParser.totalJobCount += 1

    @classmethod
    def get_job_count(cls):
        return cls.totalJobCount

    # get application name
    def get_application_tag(self):
        return self.tag

    # get job in json raw format read in from file
    def get_job_data(self):
        return self.data

    # return job dictionary
    def get_job_dictionary(self):
        return self.jobDictionary

    # return an element from job dictionary
    def get_element_dictionary(self, key):
        job_dict = self.get_job_dictionary()
        if key in job_dict:
            return job_dict[key]
        else:
            print('No key {} exists in job dictionary'.format(key))
            sys.exit(0)

    def set_job_dictionary(self, key, value):
        job_dict = self.get_job_dictionary()
        job_dict[key] = value

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
                    ingest_time = item[key][0]
        except:
            print("no Request")
        else:
            self.set_job_dictionary("ingestTime", ingest_time)

    def parse_reply(self, json_data):
        try:
            for item in json_data['results']['dmf']['reply']:
                # There is only 1 item in reply per ingest so it safe here to loop through by key
                for key in item:
                    reply_accept_time = item[key][0]
                    reply_sent_time = item[key][1]
        except:
            print("no Reply")
        else:
            self.set_job_dictionary("replyTimeAccept", reply_accept_time)
            self.set_job_dictionary("replyTimeSent", reply_sent_time)

    def parse_update(self, json_data):
        try:
            # There could be multiple actions (items) defined in workflow per ingest
            action_items = json_data['results']['dmf']['update']
        except:
            print("no Update")
        else:
            item_count = len(action_items)
            self.set_job_dictionary("actionCount", item_count)

            # loop through actions
            for index in range(item_count):
                action_index = '{}_{}'.format('actionName', index)
                task_set = action_items[index]
                self.set_job_dictionary(action_index, str(task_set.keys()[0]))

                try:
                    action_name = self.get_job_dictionary()[action_index]
                    print(task_set[action_name].keys())

                    '''
                    # set a pair of {a action name, a list of task names included} as follows
                    # key   - (action name) : ODS_BPSA_US_ALLOCATIONS_ACTION ;
                    # value - (a list of tasks): ['dmf_sdt__TRANSFORM', '__EXECUTE_ACTION', 'dmf_ingest__MOVE']
                    '''
                    self.set_job_dictionary(action_name, task_set[action_name].keys())
                    task_names = self.get_job_dictionary()[action_name]

                    # looping through each task
                    for i in range(len(task_names)):
                        a_task_name = task_names[i]
                        # print a_task_name
                        task = task_set[action_name][a_task_name]

                        '''
                        # updating each task as the following:
                        # key - task name as kay (dmf_sdt__TRANSFORM);
                        # value - is a list of items such as status, zone, times and etc. about current task:
                        #       {'dmf_sdt__TRANSFORM': ['SUCCEEDED', u'RDZ', u'TSD', u'2018-10-03T22:56:00.992272+00:00', u'2018-10-03T18:59:15.895000-04:00']},
                        #     , {'__EXECUTE_ACTION': ['ACTION_FAILED', None, None, u'2018-10-03T22:55:32.730543+00:00', u'2018-10-03T22:59:16.886432+00:00']},
                        #     , {'dmf_ingest__MOVE': ['FAILED', u'LDZ', u'RDZ', u'2018-10-03T22:55:32.888001+00:00', u'2018-10-03T22:55:33.343281+00:00']}
                        # previous a pair of {a action name, a list of task names included}
                        # become             {a action name, a list of dictionary where each task name is the key}
                        # 'ODS_BPSA_US_ALLOCATIONS_ACTION': 
                        # [
                        #   {u'dmf_sdt__TRANSFORM': ['SUCCEEDED', u'RDZ', u'TSD', u'2018-10-03T22:56:00.992272+00:00', u'2018-10-03T18:59:15.895000-04:00']}, 
                        #   {u'__EXECUTE_ACTION': ['ACTION_FAILED', None, None, u'2018-10-03T22:55:32.730543+00:00', u'2018-10-03T22:59:16.886432+00:00']}, 
                        #   {u'dmf_ingest__MOVE': ['FAILED', u'LDZ', u'RDZ', u'2018-10-03T22:55:32.888001+00:00', u'2018-10-03T22:55:33.343281+00:00']}
                        # ]
                        '''
                        try:
                            if str(a_task_name) == '__EXECUTE_ACTION':
                                task_names[i] = {a_task_name: [ 'ACTION_SUCCEEDED', None, None, task['ACTION_BEGIN'][0], task['ACTION_SUCCEEDED'][0] ]}
                            else:
                                task_names[i] = {a_task_name: [ 'SUCCEEDED', task['SUCCEEDED'][-1]['src'][:3], task['SUCCEEDED'][-1]['dest'][:3], task['BEGIN'][0], task['SUCCEEDED'][0] ]}
                        except:
                            print("Task failure hence Action failure")
                            if str(a_task_name) == '__EXECUTE_ACTION':
                                task_names[i] = {a_task_name: [ 'ACTION_FAILED', None, None, task['ACTION_BEGIN'][0], task['ACTION_FAILED'][0] ]}
                            else:
                                task_names[i] = {a_task_name: [ 'FAILED', task['FAILED'][-1]['src'][:3], task['FAILED'][-1]['dest'][:3], task['BEGIN'][0], task['FAILED'][0] ]}
                except:
                    print("no Action")

    #def generate_html(self, FLOW, INGEST_TIME, ACITION_BEGIN_TIME, ACITION_SUCCESS_TIME):
    def generate_html(self):

        html = HTML()
        html = html.html()

        style_code = "table { border-collapse: collapse; } table th { border: 1px solid #e3e3e3; text-align: center; background-color: #3a6070; color: #FFF; padding: 4px 20px 4px 8px;} table td { border: 1px solid #e3e3e3; padding: 4px 8px;} table tr:nth-child(odd) td { background-color: #e7edf0;}"

        html.style(style_code)

        head = html.head
        head.title('Performance Reports')
        head.meta(content='text/html; charset=utf-8')
        head.link(rel='stylesheet', href='main-1.css', type='text/css')

        table = html.body.table()

        t_row1 = table.tr
        t_row1.th('Application Portfolio - ' + self.get_application_tag())
        t_row1.th('INGEST REQUEST')
        t_row1.th('INGEST REPLY', colspan='2')

        t_row2 = table.tr
        t_row2.th('Job Name')
        t_row2.th('Request Time [UTC]')

        t_row2.th('Received Time [UTC]')
        t_row2.th('Reply Time [UTC]')

        t_row3 = table.tr
        t_row3.td("JOB_NAME")

        dt_request = dateutil.parser.parse(self.get_element_dictionary('ingestTime'))
        dt_reply_received = dateutil.parser.parse(self.get_element_dictionary('replyTimeAccept'))
        dt_reply_reply = dateutil.parser.parse(self.get_element_dictionary('replyTimeSent'))

        # Ingest time from client - convert it (usually based on Eastern time to DMF timezone time (utc) and then chop the date prefix
        t_row3.td(dt_request.astimezone(dt_reply_received.tzinfo).strftime('%H:%M:%S.%f'))
        t_row3.td(dt_reply_received.strftime('%H:%M:%S.%f'))
        t_row3.td(dt_reply_reply.strftime('%H:%M:%S.%f'))

        dt_action_complete = None

        # A workflow can have multi-actions so table header also need to consider dynamicallly
        for i in range(self.get_element_dictionary('actionCount')):
            # print self.get_element_dictionary('actionName_{}'.format(i))
            action_name = self.get_element_dictionary('actionName_{}'.format(i))
            tasks = self.get_element_dictionary(action_name)
            tasks_cnt = len(tasks)
            for j in range(tasks_cnt):
                task = tasks[j].keys()[0]
                t_row1.th('{} ({}->{})'.format(str(task), tasks[j][task][1], tasks[j][task][2]), colspan='3')

                t_row2.th('Begin [UTC]')
                t_row2.th('Succeed [UTC]')
                t_row2.th('Processing Time')

                dt_begin = dateutil.parser.parse(tasks[j][task][3])
                dt_complete = dateutil.parser.parse(tasks[j][task][4])
                t_row3.td(dt_begin.strftime('%H:%M:%S.%f'))
                t_row3.td(dt_complete.strftime('%H:%M:%S.%f'))

                # amazing!!! - timedelta can do the difference by observing the time zone difference!
                # dt_1: 2018 - 10 - 03T18:55:31.955000 - 04:00
                # dt_3: 2018 - 10 - 03T22:59:16.886432 + 00:00
                t_row3.td('{} {}'.format(str(dt_complete - dt_begin), "| [" + str((dt_complete - dt_begin).seconds) + "] secs"))

                if str(task) == '__EXECUTE_ACTION':
                    dt_action_complete = dt_complete

        t_row1.th('END TO END')
        t_row2.th('Total Processing Time')

        t_row3.td('{} {}'.format(str(dt_action_complete - dt_request), "| [" + str((dt_action_complete - dt_request).seconds) + "] secs"))


        '''
        t_row1 = table.tr
        t_row1.th('Application Portfolio - ' + self.get_application_tag())
        t_row1.th('INGEST REQUEST')
        t_row1.th('EXECUTE_ACTION', colspan='3')
        t_row1.th('END TO END')

        t_row2 = table.tr
        t_row2.th('Job Name')
        t_row2.th('Request Time [UTC]')
        t_row2.th('Action Begin [UTC]')
        t_row2.th('Action Success [UTC]')
        t_row2.th('Action Processing Time')
        t_row2.th('Total Processing Time')

        # convert string to datetime
        #dt_1 = dateutil.parser.parse(INGEST_TIME)
        dt_1 = dateutil.parser.parse(self.get_element_dictionary('ingestTime'))
        print dt_1

        #dt_2 = dateutil.parser.parse(ACITION_BEGIN_TIME)
        dt_2 = dateutil.parser.parse(self.get_element_dictionary('ODS_BPSA_US_ALLOCATIONS_ACTION')[1]['__EXECUTE_ACTION'][3])
        print dt_2

        #dt_3 = dateutil.parser.parse(ACITION_SUCCESS_TIME)
        dt_3 = dateutil.parser.parse(self.get_element_dictionary('ODS_BPSA_US_ALLOCATIONS_ACTION')[1]['__EXECUTE_ACTION'][4])
        print dt_3

        t_row3 = table.tr
        t_row3.td("JOB_NAME")
        # Ingest time from client - convert it (usually based on Eastern time to DMF timezone time (utc) and then chop the date prefix
        t_row3.td(dt_1.astimezone(dt_2.tzinfo).strftime('%H:%M:%S.%f'))
        t_row3.td(dt_2.strftime('%H:%M:%S.%f'))
        # t_row3.td(str(dt_3))
        t_row3.td(dt_3.strftime('%H:%M:%S.%f'))

        t_row3.td('{} {}'.format(str(dt_3 - dt_2), "| [" + str((dt_3 - dt_2).seconds) + "] secs"))

        # amazing!!! - timedelta can do the difference by observing the time zone difference!
        # dt_1: 2018 - 10 - 03T18:55:31.955000 - 04:00
        # dt_3: 2018 - 10 - 03T22:59:16.886432 + 00:00
        t_row3.td('{} {}'.format(str(dt_3 - dt_1), "| [" + str((dt_3 - dt_1).seconds) + "] secs"))
        '''


        with open('performance.html', 'w') as f:
            f.writelines(html)


if __name__ == '__main__':
    tag = str((sys.argv[1]))

    print(JobParser.totalJobCount)

    with open('json\\sample1.json', 'r') as f:
        parser = JobParser(json.load(f), tag)
        parser.parse()

    print(JobParser.get_job_count())
    parser.generate_html()
