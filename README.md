DoMyBits
========

Do Bits When Things Happen

The idea behind this program was that IFTTT wasn't completely cutting it.

For example, you couldn't say, If this, and this, then that. Or, if this and this and this then that...

SO... the idea here is that you can trigger an IFTTT recipe to do something that this will monitor and then action which in turn could fire another recipe. 

The first objective of this project is to have IFTTT trigger on a Wemo motion sensor and then have it send an email. If that email has was sent after sunset, then send an email back saying that it can switch the lights on.

Get my drift?

Obviously the concept could be adapted to do almost anything and I'm sure it will grow in time with additional python plugins.

To Install
==========

This program can run under Windows or Linux

1. Create a folder/Directory called "DoMyBits"
2. Download the zip file and extract to that folder/Directory
3. Ensure python, Mysql & mysqldb are all installed
3. Run setup.py to enter your personal settings and setup the database
4. Run DoMyBitsDaemon.py

To Schedule Events
==================

Run manageSchedule.py