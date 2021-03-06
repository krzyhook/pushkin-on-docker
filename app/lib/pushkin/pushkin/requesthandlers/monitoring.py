'''
The MIT License (MIT)
Copyright (c) 2016 Nordeus LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import tornado.web
from pushkin import context

"""Utility handlers used for monitoring the server."""


class RequestQueueHandler(tornado.web.RequestHandler):
    """Responds with number of items in RequestProcessor."""

    def get(self):
        try:
            queue_size = context.request_processor.queue_size()
            self.write(str(queue_size))
        except:
            context.main_logger.exception(
                "Could not get queue size for request processor!")
            raise tornado.web.HTTPError(400)


class ApnSenderQueueHandler(tornado.web.RequestHandler):
    """Responds with number of items in ApnSenderProcessor."""

    def get(self):
        try:
            sender_name = 'pushkin.sender.senders.ApnNotificationSender'
            queue_size = context.request_processor.sender_manager.sender_by_name[sender_name].queue_size()
            self.write(str(queue_size))
        except:
            context.main_logger.exception(
                "Could not get queue size for sender {}!".format(sender_name))
            raise tornado.web.HTTPError(400)


class GcmSenderQueueHandler(tornado.web.RequestHandler):
    """Responds with number of items in GcmSenderProcessor."""

    def get(self):
        try:
            sender_name = 'pushkin.sender.senders.GcmNotificationSender'
            queue_size = context.request_processor.sender_manager.sender_by_name[sender_name].queue_size()
            self.write(str(queue_size))
        except:
            context.main_logger.exception(
                "Could not get queue size for sender {}!".format(sender_name))
            raise tornado.web.HTTPError(400)


class NotificationPostProcessorQueue(tornado.web.RequestHandler):
    """Responds with number of items in NotificationPostProcessor."""

    def get(self):
        try:
            queue_size = context.request_processor.sender_manager.notification_post_processor.queue_size()
            self.write(str(queue_size))
        except:
            context.main_logger.exception(
                "Could not get queue size for notification post processor!")
            raise tornado.web.HTTPError(400)
