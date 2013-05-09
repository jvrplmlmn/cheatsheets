#!/usr/bin/env python

# This script implements a simple SMTP mail client, my simply sending a text file supplied
# to a supplied email address, from a given email address, with the current system date,
# using a supplied SMTP server hostname.
#

import os
import smtplib
import sys
import time
import re

class Message:
    def __init__(self, to_addr, from_addr, date_str, subject, filename, message_body ):
        self.to_addr = to_addr
        self.from_addr = from_addr
        self.date_str = date_str
        self.subject = subject
        self.filename = filename
        self.message_body = message_body

    def build_smtp_message(self):
        # FIXME Implement this so the correct SMTP formatted body is generated...
        return 'From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s' % ( self.from_addr, self.to_addr, self.subject, self.date_str, self.message_body )

    def niall():
        return(1)

    def send(self, serverAddress):
        server = smtplib.SMTP( serverAddress )
        if re.match(".*\.html$",self.filename):
            message = self.createhtmlmail()
            server.sendmail( self.from_addr, self.to_addr, message )
        else:
            server.sendmail( self.from_addr, self.to_addr, self.build_smtp_message() )
        server.quit()

    def createhtmlmail (self):
        #Create a mime-message that will render HTML in popular MUAs, text in better ones
        import MimeWriter
        import mimetools
        import cStringIO

        html = self.message_body
        text = self.message_body

        out = cStringIO.StringIO() # output buffer for our message
        htmlin = cStringIO.StringIO(html)
        txtin = cStringIO.StringIO(text)
        writer = MimeWriter.MimeWriter(out)
        #
        # set up some basic headers... we put subject here
        # because smtplib.sendmail expects it to be in the
        # message body
        #
        writer.addheader("Subject", self.subject)
        writer.addheader("MIME-Version", "1.0")
        #
        # start the multipart section of the message
        # multipart/alternative seems to work better
        # on some MUAs than multipart/mixed
        #
        writer.startmultipartbody("alternative")
        writer.flushheaders()
        #
        # the plain text section
        #
        subpart = writer.nextpart()
        subpart.addheader("Content-Transfer-Encoding", "quoted-printable")
        pout = subpart.startbody("text/plain", [("charset", 'us-ascii')])
        mimetools.encode(txtin, pout, 'quoted-printable')
        txtin.close()
        #
        # start the html subpart of the message
        #
        subpart = writer.nextpart()
        subpart.addheader("Content-Transfer-Encoding", "quoted-printable")
        #
        # returns us a file-ish object we can write to
        #
        pout = subpart.startbody("text/html", [("charset", 'us-ascii')])
        mimetools.encode(htmlin, pout, 'quoted-printable')
        htmlin.close()
        #
        # Now that we're done, close our writer and
        # return the message body
        #
        writer.lastpart()
        msg = out.getvalue()
        out.close()
        return msg

if __name__ == '__main__':
    try:
        smtp_hostname = sys.argv[1]
        fromaddr = sys.argv[2]
        toaddr = sys.argv[3]
        filename = sys.argv[4]
        subject = ' '.join( sys.argv[5:] )
        if not os.path.exists( filename ):
            raise 'File %s does not exist' % filename
        if not os.path.isfile( filename ):
            raise '%s is not a file' % filename
    except:
        print 'Failed to read required parameters: %s' % sys.exc_info()[0]
        print 'Usage: %s smtp_host fromaddress toaddress filename subject'
        print '    fromaddress should probably be known at smtp_host'
        print '    filename MUST be ascii text, which could be UUENCODED...'
        print '    subject can be multiple words long!'
        sys.exit(1)

    try:
        f = open( filename )
        filecontents = f.read()
        f.close()
        Message( toaddr, fromaddr, time.asctime(), subject, filename, filecontents ).send( smtp_hostname )
    except:
        print 'Failed to send email: %s' % sys.exc_info()[0]
        sys.exit(1)
