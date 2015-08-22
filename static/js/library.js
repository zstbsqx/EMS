
var ERR_HANDLER = {
    '0': 'ok',
};

function checkJson(json) {
    if (json['code'] == 0) {
        return true;
    } else {
        alert('Error [' + json['code'] + ']: ' + json['desc']);
        return false;
    }
}
