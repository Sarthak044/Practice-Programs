#include<stdio.h>
#include<string.h>
#include<stdlib.h>
struct node{
int data;
struct node*next;
}*start=NULL;

void insertfirst(struct node* newnode)
{
    int num1;
    while(start->next!=NULL)
    {
        newnode=(struct node*)malloc(sizeof(struct node));
        newnode->data=num1;
        printf("Enter data");
        scanf("%d",&num1);
        newnode->next=start;
        start=newnode;

    }
}
void delete_first(struct node*temp)
{
    temp=start;
    start=start->next;
    temp->start=NULL;
    free(temp);
}
void insert_end(struct node*newnode)
{
    int num2;
    newnode=(struct node*)malloc(sizeof(struct node*));
    struct node*last=start;
    printf("Enter the data");
    scanf("%d",&num2);
    newnode->data=num2;
    newnode->next=NULL;
    while(last->next!=NULL)
    {
        last=last->next;
    }
        last->next=newnodel
        return;
    }
    void delete_end()
    {

        struct node*todelete*second last node;
        todelete=start;
        second last node= start;
        while(todelete->next!=NULL)
        {
            second last node=todelete;
            todelete=todelete->next;

        }
        second last node->next=NULL;
        free(todelete)
    }

    main()
    {
        struct newNode;

    }
