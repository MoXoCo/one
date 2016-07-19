var insertReply = function(comment) {
    var c = comment;
    var template = `
        <div class="media">
            <a class="pull-left" href="#">
                <img class="media-object" src="${ c.img }" alt="">
            </a>
            <div class="media-body">
                <h4 class="media-heading">${c.username}
                    <small>${ c.timestamp }</small>
                </h4>
                ${c.content}
            </div>
        </div>
    `;
    var id = '#id-div-reply-add-' + c.reply_id;
    log('debug id ', id);
    $(id).before(template);
};


var addNewReply = function() {
    var url = window.location.search;
    log('comment id url: ', url)
    var form = {
        comment: $('#id-textarea-comment').val(),
        comment_id: url.split('?id=')[1],
    };
    var success = function (r) {
        log('login', r);
        if(r.success) {
            insertReply(r.data);
            $('#id-textarea-comment').val('')
        } else {
            log(r.message);
        }
    };
    var error = function (r) {
        log(r.message);
    };
    vip.replyAdd(form, success, error);
};