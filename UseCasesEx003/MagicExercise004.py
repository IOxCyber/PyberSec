is_magician = False
is_expert = True

# check if magician AND expert: "you are master"
if is_magician and is_expert:
  print("You are master")
# check if magician but not expert: "you'll get there."
elif is_magician and not is_expert:
  print("You'll get there.")
# else, you need magic powers.
elif not is_magician:
  print("You need magic powers")