# Rationale

Instead of loading all your environment varaibles in separate commands, I wanted to find out a way of just putting them into SSM under a convention, and just having the application load all of those secrets automatically. 

# Example

Let's say you have an application called, `friendship`. In SSM you could store different environment varaibles under the path:
```
/friendship/staging/MY_SECRET
```

And in your application you want this secret stored as `ENV['MY_SECRET']`

With these code examples, you can automatically load all the secrets into the environment variables within your app just by shimming in the code within your application startup.



I hope to add examples of loading them outside of your application runtime, but I haven't found a decent bash script that would do it yet without using some sort of dependent library or binary.


