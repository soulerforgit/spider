import hashlib

"""
设置task,fetcher可能有headers, proxies等
task_dome = {
  "fetch": {
     "url": "http://tieba.baidu.com/"
  },
  "process": {
    "callback": "detail_page"
  },
  "schedule": {
    "priority": 2
  },
  "project": "baidu",
  "taskid": "57dd16861fbeeab46001fc9d4133b164",
}
"""

md5string = lambda x: hashlib.md5(utf8(x)).hexdigest()


class Spider:
    def __init__(self):
        self.project_name = None


    def run_task(self, module, task, response):
        callback = task['process']['callback']

        run_func(func, response, task)
        return Process(task, response)




    def run_func(self, func: function, *arguments):
        func = func
        response = arguments[0]
        task = arguments[1]



    def crawl(self, url: str, *kwargs: list)-> task:
        """
        available params:
            taskid
            fetcher:
                url
                method
                data
                headers
                timeout
                cookies
                proxy
                allow_redirects

            process:
                callback

            scheduler:
                etag
                auto_recrawl
                priority
                retries
                exetime
                age
                cancel
                itag

            other:
                js_run_at
                fetch_type
                js_script
                js_viewport_width
                js_viewport_height
                load_images
                save
         """
        task = {}
        schedule_fields = ('etag', 'auto_recrawl', 'priority', 'retries', 'exetime', 'age', 'cancel', 'itag')
        fetch_fields = ('url', 'method', 'data', 'headers', 'timeout', 'cookies', 'proxy', 'allow_redirects')
        process_fields = ('callback')

        task['taskid'] = md5string(url)

        # fetcher
        for key in kwargs:
            if key in fetch_fields:
                task['fetcher'][key] = value
            elif key in process_fields:
                task['process'][key] = value
            elif key in schedule_fields:
                task['scheduler'][key] = value
        return task

