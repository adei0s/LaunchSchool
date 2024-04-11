advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

# my solution
# end = advice.find("house")
# advice = advice[:end]

# answer

advice = advice.split("house")[0]


print(advice)