Twisted on OpenShift
====================

This git repository helps you deploy a Twisted application on OpenShift.


Running on OpenShift
--------------------

Create an account at https://openshift.redhat.com/


Create a diy-0.1 application::

    rhc app create -a applicationname -t diy-0.1


Add this repo::

    cd applicationname
    git remote add upstream -m master git://github.com/bhuztez/openshift-diy-twisted-demo.git
    git pull -s recursive -X theirs upstream master


Then push::

    git push


Now checkout your application at::

    https://applicationname-$yournamespace.rhcloud.com

