#!/usr/bin/groovy
@Library('github.com/SprintHive/sprinthive-pipeline-library')

def componentName = 'python-starter-project'
def versionTag = ''
def resourcesDir = 'config/kubernetes'
def dockerImage

dockerNode(label: 'docker-builder') {

    stage('Build and Publish docker image') {
        checkout scm
        versionTag = getNewVersion {}
        dockerImage = "eu.gcr.io/jons-world/$componentName:${versionTag}"

        container('docker') {
            sh "docker build -t ${dockerImage} ."
            def img = docker.image(dockerImage)
            docker.withRegistry("https://eu.gcr.io", "gcr:honeypot-gcr-credentials") {
                img.push()
            }
        }
    }

    stage('Rollout to Development') {
        def namespace = 'dev'
        def deployStage = 'development'

        def kubeResources = kubeResourcesFromTemplates {
            templates = [
                readFile(resourcesDir + '/deployment.yaml'),
                readFile(resourcesDir + '/service.yaml'),
            ]
            stage = deployStage
            version = versionTag
            image = dockerImage
            name = componentName
        }

        for (String kubeResource : kubeResources) {
            kubernetesApply(file: kubeResource, environment: namespace)
        }
    }
}
