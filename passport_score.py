import tkinter as tk
from tkinter import messagebox

GITCOIN_PASSPORT_WEIGHTS = {
    "Brightid": "0.689",
    "CivicCaptchaPass": "1",
    "CivicLivenessPass": "2.25",
    "CivicUniquenessPass": "2.25",
    "Coinbase": "1.35",
    "CommunityStakingBronze": "1.27",
    "CommunityStakingGold": "1.27",
    "CommunityStakingSilver": "1.27",
    "Discord": "0.689",
    "Ens": "2.2",
    "EthGasProvider": "2.4",
    "EthGTEOneTxnProvider": "1.27",
    "ethPossessionsGte#1": "1.79",
    "ethPossessionsGte#10": "1.27",
    "ethPossessionsGte#32": "1.27",
    "Facebook": "0.689",
    "FacebookProfilePicture": "0.689",
    "FirstEthTxnProvider": "1.16",
    "GitcoinContributorStatistics#numGr14ContributionsGte#1": "1.41",
    "GitcoinContributorStatistics#numGrantsContributeToGte#1": "1.57",
    "GitcoinContributorStatistics#numGrantsContributeToGte#10": "2.30",
    "GitcoinContributorStatistics#numGrantsContributeToGte#100": "0.52",
    "GitcoinContributorStatistics#numGrantsContributeToGte#25": "1.48",
    "GitcoinContributorStatistics#numRoundsContributedToGte#1": "1.57",
    "GitcoinContributorStatistics#totalContributionAmountGte#10": "1.53",
    "GitcoinContributorStatistics#totalContributionAmountGte#100": "1.37",
    "GitcoinContributorStatistics#totalContributionAmountGte#1000": "1.18",
    "GitcoinGranteeStatistics#numGrantContributors#10": "0.71",
    "GitcoinGranteeStatistics#numGrantContributors#100": "0.73",
    "GitcoinGranteeStatistics#numGrantContributors#25": "0.61",
    "GitcoinGranteeStatistics#numGrantsInEcoAndCauseRound#1": "1.18",
    "GitcoinGranteeStatistics#numOwnedGrants#1": "1.10",
    "GitcoinGranteeStatistics#totalContributionAmount#100": "0.689",
    "GitcoinGranteeStatistics#totalContributionAmount#1000": "0.689",
    "GitcoinGranteeStatistics#totalContributionAmount#10000": "0.689",
    "githubAccountCreationGte#180": "1.21",
    "githubAccountCreationGte#365": "1.21",
    "githubAccountCreationGte#90": "1.21",
    "githubContributionActivityGte#120": "1.21",
    "githubContributionActivityGte#30": "1.21",
    "githubContributionActivityGte#60": "1.21",
    "GitPOAP": "1.54",
    "GnosisSafe": "2.65",
    "Google": "2.25",
    "GuildAdmin": "0.689",
    "GuildMember": "0.689",
    "GuildPassportMember": "0.689",
    "HolonymGovIdProvider": "4",
    "Hypercerts": "0.689",
    "IdenaAge#10": "1.48",
    "IdenaAge#5": "1.48",
    "IdenaStake#100k": "1.41",
    "IdenaStake#10k": "1.16",
    "IdenaStake#1k": "0.9",
    "IdenaState#Human": "1.61",
    "IdenaState#Newbie": "0.51",
    "IdenaState#Verified": "1.35",
    "Lens": "2.45",
    "Linkedin": "2.45",
    "NFT": "0.69",
    "PHIActivityGold": "1.16",
    "PHIActivitySilver": "1.67",
    "Poh": "1.21",
    "SelfStakingBronze": "1.21",
    "SelfStakingGold": "1.21",
    "SelfStakingSilver": "1.21",
    "SnapshotProposalsProvider": "2.82",
    "SnapshotVotesProvider": "1.41",
    "Twitter": "1.21",
    "TwitterFollowerGT100": "1.21",
    "TwitterFollowerGT500": "1.21",
    "TwitterFollowerGT5000": "1.21",
    "TwitterFollowerGTE1000": "1.21",
    "TwitterTweetGT10": "1.21",
    "twitterAccountAgeGte#180": "1.21",
    "twitterAccountAgeGte#365": "1.21",
    "twitterAccountAgeGte#730": "1.21",
    "twitterTweetDaysGte#30": "1.21",
    "twitterTweetDaysGte#60": "1.21",
    "twitterTweetDaysGte#120": "1.21",
    "ZkSync": "0.400",
    "ZkSyncEra": "0.400",
}

def calculate_score(stamps):
    total_score = 0
    for stamp in stamps:
        if stamp in GITCOIN_PASSPORT_WEIGHTS:
            total_score += float(GITCOIN_PASSPORT_WEIGHTS[stamp])
    return round(total_score, 2)  # Round the total score to 2 decimal places

def calculate():
    selected_stamps = [var.get() for var in checkboxes if var.get()]
    score = calculate_score(selected_stamps)
    messagebox.showinfo('Score', f'Your score is: {score}')

def clear_selection():
    for var in checkboxes:
        var.set('')

root = tk.Tk()

# Create a frame to hold the checkboxes
frame = tk.Frame(root)
frame.pack()

# Create a label for the title
title = tk.Label(frame, text="Gitcoin Passport’s score", font=("Arial", 20))
title.grid(row=0, column=0, columnspan=3)

# Determine the number of items per column
items_per_column = 25

# Create the checkboxes inside the frame
checkboxes = []
for i, (stamp, weight) in enumerate(GITCOIN_PASSPORT_WEIGHTS.items()):
    var = tk.StringVar()
    chk = tk.Checkbutton(frame, text=f"{stamp} ({weight})", variable=var, onvalue=stamp, offvalue="", anchor='w')
    chk.grid(row=(i % items_per_column)+1, column=i // items_per_column, sticky='w')
    checkboxes.append(var)

# Create the buttons inside the frame
calculate_btn = tk.Button(frame, text="Calculate Score", command=calculate, font=("Arial", 15))
calculate_btn.grid(row=items_per_column+10+1, column=0, pady=10, padx=10)

clear_btn = tk.Button(frame, text="Clear Selection", command=clear_selection, font=("Arial", 15))
clear_btn.grid(row=items_per_column+10+1, column=1, pady=10, padx=10)

root.mainloop()
