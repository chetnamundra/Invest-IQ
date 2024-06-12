import csv

current_affairs = """
1. Sensex's next target is 1 lakh under Nirmala's second regime as FM
2. MS bullish on 4 gas stocks if natural gas attracts GST
3. BoB to IDBI need to wait for ₹6,200 cr from Go First
4. EVs have a new challenge to deal with the thieves
5. What Hinduja scion said in human-trafficking trial?
6. ET MARKETS
7. Economist predicts a 2025 stock market crash
8. Sanjiv Bhasin on 3 IT stocks that may outperform
9. Nifty hits fresh high; Sensex surges 500 pts
10. StockTalk: Get your query answered by expert
11. Andhra gets new govt as Naidu, cabinet take oath
12. Installing solar panels in Delhi to get easier
13. SC pulls up AAP govt for inaction on tanker mafia
14. 3 attacks in 3 days: Terror strikes again in J&K
15. ICICI Bnk to stop these credit card charges from Jul
16. Chandrababu Naidu takes oath as Andhra CM; now, he needs to find funds to keep his poll promises
17. 90% Indian employees suffering, 40% sad: Report
18. Pak misses growth target, but donkey population rises
19. Motor insurance new rule: No arbitrary claim rejection
20. Can Pakistan make it to the Super 8 round in T20 WC?
21. 'Jobs are not a problem': Panagariya's Budget tip to FM
22. Beyond TDP euphoria! Andhra-linked stocks that are worth buying for the long term
23. ITR: When will you get Form 16 from your employer?
24. Govt sharpens rural focus, readies plan for jobs, roads
25. This city to mandate EV charging for new buildings
26. Lt Gen Upendra Dwivedi next Chief of Army Staff
27. Sebi bans former TV anchor Pandya, 7 others for 5 yrs
28. Too taxing to cross: Chinese EVs to be hit with multi-billion-euro tariffs at EU toll gates
29. DA hike for bank employees; 5-day bank week update
30. Mastering data analytics for business
31. AI is making robots smarter. They’ll need boundaries
32. Mohan Charan Majhi: Meet the next CM of Odisha
33. No stay, SC seeks NTA response on paper leak charge
34. Banks seek changes in blanket infra provisions
35. Scoop: Investors line up for financing round valuing Zepto at about $3 billion
36. Ministers who won, but still didn't make it to Modi 3.0
37. Not many investors enthused by Apple
38. Former banker banking on past experience in ministry
39. India's new brain power adding to its economic brawn
40. T20 World Cup: Pakistan chase 107 to beat Canada
41. Smallcaps: Don't be afraid of narrative against them, but surely check critical points: 5 stock from different sectors for long-term investors
42. TRADERS’ CORNER: IT services player in mobile space ready to pocket 12% gains; energy stock set for 7% boost
43. Stock Radar: This pharma stock sees mild consolidation after 130% rally in 1 year; time to buy the dip?
44. WinZO vs. Hike: Kavin Mittal dragged to arbitration over alleged IP breach
45. How PTC, PFS used INR1 crore company funds to save Pawan Singh
46. One key risk with Cognizant’s M&A deal
47. IPL's biz value up 6.5% to $16.4 bn in 2024
48. Modi 3.0 fixes date for 1st parliament meet
49. Indians are loving visa-free holidays
50. Gold prices drive Indians towards diamonds
51. UK economy shows no growth in April
52. Tata reveals launch timeline of upcoming EVs
53. Hyundai Motor teases new EV, the Inster
54. Naidu won a political battle in Andhra
55. EV sales soar 40.31 per cent in FY24
56. New Cabinet: Who got what? Check here
57. Boeing's puzzle: Is it time for a new plane?
58. Modi 3.0 growth story, to be continued
59. SA 1st team to get qualify for T20 WC Super 8
60. Schengen visas get costlier from today
61. Uttarakhand Tourism teams with Prime Focus Technologies
62. T20 WC: Sri Lanka's Super 8 ticket in doubt
63. WHO confirms human case of bird flu in India
64. Paramount-Skydance merger talks called off
65. Siam seeks GST reduction on two-wheelers
66. Wipro Consumer CEO bullish on rural
67. Two options on calendar for budget session
68. Buyers return to stores as gold prices cool down"""


def extract_and_save_data(stock_data):
    print(stock_data)


def read_stock_data_from_csv(csv_file):
    stock_data = []
    with open(csv_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stock_data.append(row)
    return stock_data
