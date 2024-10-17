Go to [https://github.com/suraj0-11/jenkin-example.git](https://github.com/suraj0-11/jenkin-example.git) for the script code.

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
```
## 🛠️ Step 2: Slack Notification Integration

1. **Install Slack Notification Plugin**
   - Navigate to **Manage Jenkins** > **Plugins** > **Available plugins** and search for the Slack Notification plugin. Install it.

   ![Slack Plugin](./images/slack-plugin.png) <!-- Placeholder for plugin installation image -->

2. **Configure Slack Settings**
   - Go to **Manage Jenkins** > **Configure System**. Scroll to the **Slack** section and enter your workspace credentials (Webhook URL, Channel, etc.).

   ![Slack Configuration](./images/slack-configuration.png) <!-- Placeholder for Slack configuration image -->

3. **Integrate Jenkins with Slack App**
   - In your Slack app, add the **Jenkins CI** integration and generate a token.
   - Copy the token and add it as a secret in Jenkins under **Credentials**.

   ![Slack Integration](./images/slack-integration.png) <!-- Placeholder for Slack integration image -->
   ![Slack Integration](./images/slack-integration1.png) <!-- Placeholder for Slack integration image -->
   ![Slack Integration](./images/slack-integration2.png) <!-- Placeholder for Slack integration image -->

4. **Save the Configuration**
   - After entering the credentials and token, click **Save** to finalize the integration.


## 💻 Step 3: Run the Pipeline

1. **Create Pipeline Job**
   - Go back to your pipeline project in Jenkins, and add the Git repository link (`https://github.com/suraj0-11/jenkin-example.git`).

   ![Add Git Repository](./images/git-repository.png) <!-- Placeholder for Git repository image -->

2. **Choose the Jenkinsfile**
   - In the pipeline configuration, specify the appropriate `Jenkinsfilepass` for successful builds and `Jenkinsfilefail` for failures.

3. **Run the Pipeline**
   - Save and trigger the pipeline job. Jenkins will execute the pipeline and send notifications to Slack based on the outcome (success or failure).

   ![Pipeline Run](./images/pipeline-run.png) <!-- Placeholder for Pipeline run image -->

4. **Check Slack Notifications**
   - Once the pipeline finishes, check the Slack channel `#all-slack` for the success or failure notification.

   ![Slack Notification](./images/slack-notification.png) <!-- Placeholder for Slack notification image -->




