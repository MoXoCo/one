from flask import render_template
from flask import request
from ..models import Post

from . import main
PER_PAGE_NUMS = 3

@main.route('/')
def index_view():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.title.desc()).paginate(
        page,
        per_page=PER_PAGE_NUMS,
        error_out=False
    )
    posts = pagination.items
    return render_template('index.html',
                           posts=posts,
                           pagination=pagination)


@main.route('/posts/<post_id>')
def post_view(post_id):
    post = Post.query.get_or_404(post_id)
    pagination = Post.query.order_by(Post.title.desc()).filter(
        Post.title<=post.title).paginate(
        page=1,
        per_page=PER_PAGE_NUMS)
    return render_template('post.html',
                           post=post,
                           pagination=pagination)