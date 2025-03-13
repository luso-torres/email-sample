from email_service import EmailService

class Smtp(EmailService):
    def __init__(self, smtp_server:str, signature:str="") -> None:
        self.smtp_server = smtp_server
        self.signature = signature

    def send_email(self, to_address: str, subject: str, body: str) -> str:
        formatted_body = f"{body}\n\n-- {self.signature}"
        return f"Sending email to {to_address} usgin SMTP with subject '{subject}' and body: {formatted_body}"
    
    class SendGrid(EmailService):
        def send_email(self, to_address: str, subject: str, body: str) -> str:
            return f"Sending email to {to_address} using SendGrid with subject '{subject}' and body {body}"

    class MailChimp(EmailService):
        def __init__(self, attachment: str="") -> None:
            self.attachment: str = attachment
        
        def send_email(self, to_address: str, subject: str, body: str) -> str:
            base_message = f"Sent email to {to_address} with subject 'subject' and body: {body}"
            if self.attachment:
                return base_message + f"with attachment {self.attachment}"