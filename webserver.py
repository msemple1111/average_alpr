from main import *
from bottle import route, run, request
@route('/api/camera/1', method='POST')
def camera_1():
    #post data should look like (in any order) '{"road":1, "plate":"YS54 GBF","time": 1442862678}'
    #                                           (road id,   number plate,      time in unix epoch)
    valid = validate()
    road, plate, time = valid.postdata(request.body.read())
    return request.body.read()
    #return str(road),'\n', plate,'\n', str(time), '\n'

    
run(host='0.0.0.0', port=8080)