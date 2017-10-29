BEGIN {FS="\t"; OFS = "**"}
$4 == "South America" {$4 = "SA"}
$4 == "North America" {$4 = "NA"}
{print}
