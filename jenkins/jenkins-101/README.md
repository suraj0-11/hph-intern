## 📝 Step 1: Configuring Jenkins Pipeline

1. **Navigate to Jenkins Dashboard**
   - From the Jenkins dashboard, click on **New Item** and create a new pipeline project.

2. **Configure the Pipeline**
   - Select **Pipeline** as the project type.

   ![Configure Section](./images/configure-section.png) <!-- Placeholder for configure section image -->

3. **Add Git Repository**
   - In the pipeline configuration, under **Source Code Management (SCM)**, select **Git** and provide your repository link.

   ![Git SCM Section](./images/git-scm-section.png) <!-- Placeholder for Git SCM section image -->

4. **Jenkinsfile Setup**
   - Create a `Jenkinsfile` in your repository for the pipeline script:
   
   - For success, create `Jenkinsfilepass`:
   ```groovy
   pipeline {
       agent any
       stages {
           stage('Build') {
               steps {
                   echo 'Building...'
               }
           }
           stage('Test') {
               steps {
                   echo 'Testing...'
               }
           }
           stage('Deploy') {
               steps {
                   echo 'Deploying...'
               }
           }
       }
       post {
           success {
               slackSend (channel: '#all-slack', message: 'Pipeline passed!')
           }
       }
   }
For failure, create Jenkinsfilefail:
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
    post {
        failure {
            slackSend (channel: '#all-slack', message: 'Pipeline failed!')
        }
    }
}

You can replace the `![...]` with actual image links later when you upload them.
