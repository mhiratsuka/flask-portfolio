from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from myportfolio import db
from myportfolio.models import Post
from myportfolio.posts.forms import PostForm
from myportfolio.posts.utils import save_work_picture, save_post_picture, save_post_video


posts = Blueprint('posts', __name__)

@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        workpicture = save_work_picture(form.workpicture.data)
        if form.postpicture.data:
            postpicture = save_post_picture(form.postpicture.data)
        else:
            postpicture = None
        if form.postvideo.data:
            postvideo = save_post_video(form.postvideo.data)
        else:
            postvideo = None
        post = Post(worktitle=form.worktitle.data, category=form.category.data, content=form.content.data, author=current_user, workpicture=workpicture, 
workpicture_name=form.workpicture_name.data, date_developed=form.date_developed.data, site_link=form.site_link.data, site_description=form.site_description.data, 
postpicture=postpicture, postpicture_name=form.postpicture_name.data, postvideo=postvideo, postvideo_name=form.postvideo_name.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created', 'success')
        return redirect(url_for('main.work'))
    return render_template('create_post.html', title='New Post', form=form)


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.worktitle, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():

        if form.workpicture.data:
            workpicture = save_work_picture(form.workpicture.data)
            post.workpicture = workpicture 

        if form.postpicture.data:
            postpicture = save_post_picture(form.postpicture.data)
            post.postpicture = postpicture

        if form.postvideo.data:
            postvideo = save_post_video(form.postvideo.data)
            post.postvideo = postvideo

        post.worktitle = form.worktitle.data 
        post.category = form.category.data 
        post.content = form.content.data 
        post.date_developed = form.date_developed.data
        post.workpicture_name = form.workpicture_name.data 
        post.site_link = form.site_link.data 
        post.site_description = form.site_description.data 
        post.postpicture_name = form.postpicture_name.data
        post.postvideo_name = form.postvideo_name.data 
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.worktitle.data = post.worktitle
        form.category.data = post.category
        form.content.data = post.content
        form.date_developed.data = post.date_developed
        form.workpicture.data = post.workpicture 
        form.workpicture_name.data = post.workpicture_name
        form.site_link.data = post.site_link
        form.site_description.data = post.site_description
        form.postpicture.data = post.postpicture
        form.postpicture_name.data = post.postpicture_name
        form.postvideo.data = post.postvideo
        form.postvideo_name.data = post.postvideo_name
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('main.work'))
