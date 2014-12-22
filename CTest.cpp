#include <iostream>
#include <cmath>

using namespace std;

class obstacle
{
private:
    int xpos;
    int ypos;
public:
    obstacle(int x,int y)
    {
        xpos=x;
        ypos=y;
    }
    int getXstart()
    {
        return xpos;
    }
    int getYstart()
    {
        return ypos;
    }
};

int main()
{
   const int targ_xPos=rand()%500;
   const int targ_yPos=rand()%500;
   obstacle* obs[15];
    for(int i=0;i<15;i++)
    {
        obs[i]=new obstacle(rand()%499+1,rand()%499+1);
    }
    Player* p;
    while(true)
    {
        for(int i=0;i<15;i++)
        {
         if(p->xpos()==obs[i]->getXstart()&&p->yPos()==obs[i]->getYstart())
         {
             cout<<"collisions at x:"<<obs[i]->getXstart()<<" , y:"<<obs[i]->getYstart();
             exit(1);
         }
        }
           if(p->xpos()==targ_xPos&&p->ypos()==targ_yPos)
               cout<<"test passed";
            exit(1);
        
    }
}
