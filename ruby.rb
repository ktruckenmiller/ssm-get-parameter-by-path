require 'aws-sdk'

ssm_path = "/{your_deployable_name}/#{ENV['ENVIRON']}"

secrets = []
# Ruby paginates nicely!
ssm = Aws::SSM::Client.new(region: ENV['AWS_REGION'])
ssm.get_parameters_by_path(
    path: ssm_path,
    with_decryption: true
).each do |response|
  secrets.push(*response.parameters)
end

secrets.each { | secret |
  ENV[secret.name.split('/')[-1]] = secret.value
}
