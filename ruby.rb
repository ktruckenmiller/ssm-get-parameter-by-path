require 'aws-sdk'

ssm_path = "/#{DEPLOYABLE_NAME}/#{ENV['ENVIRON']}"


ssm = Aws::SSM::Client.new(region: ENV['AWS_REGION'])
secrets = ssm.get_parameters_by_path({
    path: ssm_path,
    with_decryption: true
  })

secrets.parameters.each { | secret |
  ENV[secret.name.split('/')[-1]] = secret.value
}
