from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from StandardDjangoProject.settings import BASE_URL


def send_email_confirmation_to_user(company_email, appointment):
    print("base url: ", BASE_URL)
    print("email: ", appointment.email)
    print("date: ", appointment.date)

    subject = "Your Appointment Details"
    context = {
        'appointment': appointment,
        'base_url': BASE_URL
    }
    html_message = render_to_string('appointments/email_template.html', context)
    plain_message = strip_tags(html_message)
    from_email = company_email
    to = appointment.email
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    print('email send')