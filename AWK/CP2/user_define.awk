$4 == "Asia" {pop += $3; count += 1}
END {printf "%d Asia countries have %d population in all.",count,pop}
