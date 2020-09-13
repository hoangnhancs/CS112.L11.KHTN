def kadane(seqs):
  max_sum_present = 0
  max_ending_at = 0
  start_index = 0
  start_temp = -1
  ending_index = 0
  for i in range(len(seqs)):
    max_ending_at += seqs[i]
    if (max_ending_at < 0):
      max_ending_at = 0
      start_temp = -1
    else:
      if start_temp == -1:
        start_temp = i
      if max_sum_present < max_ending_at:
        max_sum_present = max_ending_at
        start_index = start_temp
        ending_index = i
  print(start_index+1, ending_index+1, max_sum_present)
  #print(start_index+1)
  #print(ending_index+1)

#a = [2, -4, 5, -8, 4, -1, -1, 1, 1, 1, -2, 2, 4, -6, 9, -4]
n = input()
n = int(n)
a = list(map(int, input().split()))

kadane(a)
