# James Carlson 
# Coding Temple - SE FT-144
# Backend Module 3 Lesson 3 Assignment: Sets

print("\n====== 1. Python Sets Adventure ======\n")

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

print("Destinations both our airline and our competitor fly to:", our_routes.intersection(competitor_routes))
print("Destinations only our airline flys to:", our_routes.difference(competitor_routes))
print("Destinations neither airline shares:", our_routes.symmetric_difference(competitor_routes))


print("\n====== 2. Set Operations in Data Analysis ======\n")

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
print("Duplicates removed from customer_ids:", sorted({c for c in customer_ids}))