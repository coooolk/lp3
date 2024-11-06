// Online C++ compiler to run C++ program online
#include<iostream>
using namespace std;

void fibonacci(int num){
    int a = 0;
    int b = 1;
    if(num==0){
        cout<<a;
        return;
    }
    cout<<a<<" "<<b<<" ";
    for(int i=1;i<num-1;i++){
        int c = a+b;
        a=b;
        b=c;
        cout<<c<<" ";
    }
}

int rec_fibonacci(int num){
    if(num==1){
        return 1;
    }else if(num==0){
        return 0;
    }
    return rec_fibonacci(num-1) + rec_fibonacci(num-2); 
    
}

int main(){
    int n;
    cout<<"ENter a number : ";
    cin>>n;
    
    cout<<"Non Recuesive call : ";
    fibonacci(n);
    cout<<endl;
     cout<<"Recuesive call: ";
    int num = rec_fibonacci(n);
    cout<<num;
}