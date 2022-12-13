def calc(sale1, sale2, sale3, sale4):
    total_sales = sale1+sale2+sale3+sale4
    commisionamt = 0
    if total_sales >= 50000:
        commisionamt = total_sales*0.05
    remarks = ""
    if total_sales >= 80000:
        remarks = "Excellent"
    elif total_sales >= 60000:
        remarks = "Good"
    elif total_sales >= 40000:
        remarks = "Average"
    elif total_sales < 40000:
        remarks = "Work Hard"

    return total_sales, commisionamt, remarks

if __name__ == "__main__":
    sale1 = int(input("Enter the sales for week 1: "))
    sale2 = int(input("Enter the sales for week 2: "))
    sale3 = int(input("Enter the sales for week 3: "))
    sale4 = int(input("Enter the sales for week 4: "))
    tot_sales, commision, remarks = calc(sale1, sale2, sale3, sale4)
    print("total sales : rs",tot_sales)
    print("total comission: rs",commision)
    print("Remarks:", remarks)
