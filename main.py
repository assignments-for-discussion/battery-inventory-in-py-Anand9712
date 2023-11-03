
def count_batteries_by_health(present_capacities):
  counts={    #creating the dictionary for track the frequency of each battery health
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  for capacity in present_capacities:
    SoH = (capacity / 120) * 100  # Calculate State of Health (SoH) for each battery
    if SoH > 80: #SoH more than 80%, up to 100%: classified as healthy
      counts["healthy"] += 1
    elif SoH >= 62: #SoH between 80% and 62%: classified as exchange
      counts["exchange"] += 1
    else: #SoH below 62%: classified as failed
      counts["failed"] += 1
    
  return counts 


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
   # Test case 1: All batteries are healthy
  present_capacities = [120, 120, 120]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 3)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 0)

   # Test case 2: All batteries are failed
  present_capacities = [0, 30, 50]
  counts = count_batteries_by_health(present_capacities)    
  assert(counts["healthy"] == 0)
  assert(counts["exchange"] == 0)
  assert(counts["failed"] == 3)

  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
