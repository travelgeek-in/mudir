let host="";
let s3location = ''
if (process.env.NODE_ENV !== "production")
{
    host = 'http://0.0.0.0:8000',
    s3location = ''
}

export default {
    s3:s3location,
    base:host,
    login: host+'/login/',
    getUser:host+'/getUser/'
}