{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "61fc7ce4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5]\n",
      "[1, 2, 3, 4, 5, 6]\n",
      "[1, 2, 4, 5, 6] element 3 mentioned not index it is the element removed\n",
      "Updated list is : [9, 2, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "#creating list \n",
    "my_list=[1,2,3,4,5]\n",
    "#displaying list\n",
    "print(my_list)\n",
    "#adding an element to a list \n",
    "my_list.append(6)\n",
    "##displaying list\n",
    "print(my_list)\n",
    "#removing an element from list\n",
    "my_list.remove(3)\n",
    "print(my_list,\"element 3 mentioned not index it is the element removed\")#will remove element from index 3\n",
    "#modifying list element of a particular index\n",
    "my_list[0]=9\n",
    "print(\"Updated list is :\",my_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fe3783a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Name': 'Jack', 'Age': 90, 'City': 'Delhi'}\n",
      "{'Name': 'Jack', 'Age': 90, 'City': 'Delhi', 'Gender': 'Male'}\n",
      "{'Name': 'Jack', 'City': 'Delhi', 'Gender': 'Male'}\n",
      "Updated dictionary : {'Name': 'Jack', 'City': 'NewDelhi', 'Gender': 'Male'}\n"
     ]
    }
   ],
   "source": [
    "#creating dictionary\n",
    "my_dict={'Name':'Jack','Age':90,'City':'Delhi'}\n",
    "#displaying dictionary\n",
    "print(my_dict)\n",
    "#adding key value \n",
    "my_dict['Gender']='Male'\n",
    "print(my_dict)\n",
    "#removing element\n",
    "del my_dict['Age']\n",
    "print(my_dict)\n",
    "#modifying dictionary \n",
    "my_dict['City']='NewDelhi'\n",
    "print('Updated dictionary :',my_dict)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ec385a99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Set is : {1, 2, 3, 4, 5, 6, 7}\n",
      "{1, 2, 3, 4, 5, 6, 7, 8}\n",
      "{1, 2, 3, 4, 6, 7, 8}\n",
      "Updated set is : {1, 2, 3, 4, 6, 7, 8, 10}\n"
     ]
    }
   ],
   "source": [
    "#creating set \n",
    "my_set={1,2,3,4,5,6,7}\n",
    "print('Set is :',my_set)\n",
    "#adding \n",
    "my_set.add(8)\n",
    "print(my_set)\n",
    "#removing element\n",
    "my_set.remove(5)\n",
    "print(my_set)\n",
    "#modifying \n",
    "my_set.add(10)\n",
    "print(\"Updated set is :\",my_set)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9bd4249",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
