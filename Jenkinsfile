#!/usr/bin/groovy
@Library('github.com/SprintHive/sprinthive-pipeline-library')

def componentName = 'python-starter-project'
standardPythonDeploy([
        releaseName:  "python-starter",
        componentName: componentName,
        dockerTagBase: "eu.gcr.io/jons-world",
        registryUrl: "https://eu.gcr.io",
        registryCredentialsId: "gcr:honeypot-gcr-credentials"
    ])
