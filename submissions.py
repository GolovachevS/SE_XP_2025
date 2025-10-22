import os, uuid
from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from models import db, Submission, User
from forms import HWUploadForm, ReviewForm
from decorators import roles_required


from flask import send_from_directory

submissions_bp = Blueprint('submissions', __name__, url_prefix='')

@submissions_bp.route('/submit', methods=['GET', 'POST'])
@login_required
@roles_required('student')
def upload_homework():
    form = HWUploadForm()
    form.teacher_id.choices = [(u.id, u.name) for u in User.query.filter_by(role='teacher').all()]

    if form.validate_on_submit():
        f = form.file.data
        safe_name = secure_filename(f.filename)
        unique_name = f"{current_user.id}_{uuid.uuid4().hex}_{safe_name}"
        os.makedirs(current_app.config.get('UPLOAD_FOLDER', 'uploads'), exist_ok=True)
        path = os.path.join(current_app.config.get('UPLOAD_FOLDER', 'uploads'), unique_name)
        f.save(path)

        sub = Submission(
            student_id=current_user.id,
            teacher_id=form.teacher_id.data,
            stored_filename=unique_name,
            original_filename=safe_name,
        )
        db.session.add(sub)
        db.session.commit()
        flash('Файл отправлен преподавателю!', 'success')
        return redirect(url_for('submissions.upload_homework'))

    return render_template('upload_form.html', form=form)


@submissions_bp.route('/submissions/all')
@login_required
@roles_required('teacher')
def all_submissions():
    items = (
        Submission.query
        .filter(Submission.teacher_id == current_user.id)
        .order_by(Submission.submitted_at.desc())
        .all()
    )
    return render_template('all_submissions.html', items=items)


@submissions_bp.route('/submissions/<int:sid>/review', methods=['GET', 'POST'])
@login_required
@roles_required('teacher')
def review_submission(sid):
    sub = Submission.query.get_or_404(sid)
    form = ReviewForm(obj=sub)
    if form.validate_on_submit():
        sub.grade = form.grade.data
        sub.feedback = form.feedback.data
        sub.status = 'reviewed'
        db.session.commit()
        flash('Оценка и комментарий сохранены', 'success')
        return redirect(url_for('submissions.all_submissions'))
    return render_template('review_submission.html', sub=sub, form=form)




@submissions_bp.route('/uploads/<path:filename>')
@login_required
def uploaded_file(filename):
    """Позволяет скачивать/просматривать отправленные файлы"""
    upload_folder = current_app.config.get('UPLOAD_FOLDER', 'uploads')
    return send_from_directory(upload_folder, filename, as_attachment=True)


