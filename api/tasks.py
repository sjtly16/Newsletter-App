from celery import shared_task
from django.core.mail import EmailMessage
@shared_task
def send_message(email_count, recipients, html_content, subject):
    if email_count > 50:
        batches = [recipients[i:i + 50] for i in range(0, email_count, 50)]
        for batch in batches:
            msg = EmailMessage(subject, html_content,
                                from_email="team@dsckiet.com", bcc=batch, headers={
                                    "x-priority": "1",
                                    "x-msmail-priority": "High",

                                })
            msg.content_subtype = "html"  # Main content is now text/html
            email_response = msg.send()
        return None

    else:
        msg = EmailMessage(subject, html_content,
                            from_email='team@dsckiet.com', bcc=recipients, headers={
                                "x-priority": "1",
                                "x-msmail-priority": "High",
                                
                            })
        msg.content_subtype = "html"  # Main content is now text/html
        email_response = msg.send()
        return None
