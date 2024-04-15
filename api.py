from flask import Flask, render_template, redirect, request
from groceryListSRC import groceryList
from math import ceil

app = Flask(__name__)

cache = {"itemList": [], "cost": 0}

@app.route("/", methods =["GET", "POST"])
def init():
   if request.method == "POST":
      valid_customer_vec = (request.form.get("valid_customers")).split()
      tax = float(request.form.get("tax"))
      cache["gl"] = groceryList(valid_customer_vec, tax)
      return redirect("/list")
   return render_template("init.html")

@app.route("/list", methods =["GET", "POST"])
def listPage():
   vc = "Valid Customers: " + " ".join(list((cache["gl"].customer_dict).keys()))
   tax = "Tax: " + str(cache["gl"].tax * 100) + "%"
   if request.method == "POST":
      if request.form['submit_button'] == 'Add To List':
         name = request.form.get("name")
         price = float(request.form.get("price"))
         quantity = int(request.form.get("quantity"))
         customers = request.form.get("customers")
         if customers == "all":
            customer_list = list(cache["gl"].customer_dict.keys())
         else:
            customer_list = customers.split()
         cache["gl"].push_back(name, price, quantity, customer_list)
         cache["itemList"].append(cache["gl"].items[-1].toString())
         cache["cost"] = cache["gl"].total
         return render_template("list.html", itemList=cache["itemList"], cost=cache["cost"], vc=vc, tax=tax)
      elif request.form['submit_button'] == 'Finalize List':
         return redirect("/summary")
   return render_template("list.html", vc=vc, tax=tax)

@app.route("/summary", methods =["GET"])
def finalSummary():
   vc = "Valid Customers: " + " ".join(list((cache["gl"].customer_dict).keys()))
   tax = "Tax: " + str(cache["gl"].tax * 100) + "%"
   finalSumm = []
   finalSumm.append("The total cost is $" +  str(ceil(cache["gl"].total * 100) / 100.0 ))
   for customer in list((cache["gl"].customer_dict).keys()):
         finalSumm.append(customer + " owes $" + str(cache["gl"].customer_dict[customer]))
   return render_template("summ.html", itemList=cache["itemList"], cost=cache["cost"], vc=vc, tax=tax, finalSumm=finalSumm)