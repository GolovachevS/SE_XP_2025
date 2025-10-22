import os, uuid
from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from models import db, Submission, User
from forms import HWUploadForm
from decorators import roles_required

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
