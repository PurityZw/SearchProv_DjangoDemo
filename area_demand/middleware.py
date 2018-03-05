
class MyMidelleware(object):
    def process_request(self, request):
        print('process_request')