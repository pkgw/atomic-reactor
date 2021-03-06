"""
Copyright (c) 2015 Red Hat, Inc
All rights reserved.

This software may be modified and distributed under the terms
of the BSD license. See the LICENSE file for details.


It returns content of dockerfile and therefore displays it in results.
"""
from atomic_reactor.plugin import PreBuildPlugin
from atomic_reactor.util import df_parser


class CpDockerfilePlugin(PreBuildPlugin):
    key = "dockerfile_content"

    def __init__(self, tasker, workflow):
        """
        constructor

        :param tasker: DockerTasker instance
        :param workflow: DockerBuildWorkflow instance
        :return:
        """
        # call parent constructor
        super(CpDockerfilePlugin, self).__init__(tasker, workflow)

    def run(self):
        """
        try open dockerfile, output an error if there is one
        """
        try:
            return df_parser(self.workflow.builder.df_path, workflow=self.workflow).content
        except (IOError, OSError) as ex:
            return "Couldn't retrieve dockerfile: %r" % ex
