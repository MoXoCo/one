var insertComment = function(comment) {
    var c = comment;
    var template = `
        <div class="media" id="id-div-add" data-id="${c.post_id}">
            <a class="pull-left" href="#">
                <img class="media-object" src="${ c.img }" alt="">
            </a>
            <div class="media-body">
                <h4 class="media-heading">${c.username}
                    <small>${ c.timestamp }</small>
                </h4>
                ${c.content}
                <div class="post-footer">
                    <a href="?id=${c.id}#ct1">
                        <span class="label label-success" id="id-span-reply">回复</span>
                    </a>
                </div>
            </div>
        </div>
        <hr>
    `;
    $('#id-div-comments').append(template);
};

var addNewComment = function() {
    var form = {
        comment: $('#id-textarea-comment').val(),
        post_id: $('#id-div-comments').attr('data-id'),
    };
    log('form: ', form)
    var success = function (r) {
        log('login', r);
        if(r.success) {
            insertComment(r.data);
            $('#id-textarea-comment').val('')
        } else {
            log(r.message);
        }
    };
    var error = function (r) {
        log(r.message);
    };
    vip.commentAdd(form, success, error);
};
