public class test_iPlusPlus{
    private int count;
    public test_iPlusPlus(int i){
        this.count = i;
    }

    public int geti(){
        return this.count;
    }
    public int plusplusi(){
        ++this.count;
        return this.count;
    }
    public int iplusplus(){
        this.count++;
        return this.count;
    }
    public static void main(String[] args){
        test_iPlusPlus p;
        p = new test_iPlusPlus(9);
        System.out.println(p.plusplusi());
        System.out.println(p.geti());
        System.out.println(p.iplusplus());
        System.out.println(p.geti());

        }
    }
