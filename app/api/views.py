from flask import request
from flask import jsonify

from mylog import log
from . import api
from ..models import Post
from ..models import Comment


@api.route('/posts/search', methods=['POST'])
def post_search():
    form = request.get_json()
    title = form.get('title', '')
    post = Post.query.filter_by(title=title).first()
    response = dict(
        success=False,
    )

    if len(title) != 0:
        d = dict(
            success=True,
            post_id=post.id,
        )
        response.update(d)
    elif len(title) == 0:
        response['message'] = '用户没输入数据！'
    elif post is None:
        response['message'] = '数据库没有用户查找的数据！'
    log('/post/search response: ', response)
    return jsonify(response)


@api.route('/comments/edit/<post_id>', methods=['POST'])
def comment_edit(post_id):
    post = Post.query.get_or_404(post_id)
    form = request.get_json()
    content = form.get('comment', '')
    response = dict(
        success=False,
    )

    if len(content) != 0:
        c = Comment(content)
        c.post = post
        c.save()
        log('评论发表成功')
        d = dict(
            success=True,
            data=c.json(),
        )
        response.update(d)
    else:
        response['message'] = '用户没输入数据！'
    log('/comment/edit response: ', response)
    return jsonify(response)
    #return redirect(url_for('post_view', post_id=post_id))


@api.route('/comments/reply/<comment_id>', methods=['POST'])
def reply(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    form = request.get_json()
    content = form.get('comment', '')
    response = dict(
        success=False,
    )

    if len(content) != 0:
        c = Comment(content)
        c.post = comment.post
        c.reply_id = comment_id
        c.save()
        log('评论发表成功')
        d = dict(
            success=True,
            data=c.json(),
        )
        response.update(d)
    else:
        response['message'] = '用户没输入数据！'
    log('/comment/edit response: ', response)
    return jsonify(response)







