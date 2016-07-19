var searchPost = function() {
    var title = $('#id-input-search').val();
    var form = {
        title: title
        }
    var success = function(r) {
        if(r.success){
            var url = '/posts/' + r.post_id;
            log('get success, ', url, r);
            window.location.href = url
        } else {
            log(r.message);
        }
    };
    var error = function (err) {
        log(err);
    };
    vip.postSearch(form, success, error);
};

