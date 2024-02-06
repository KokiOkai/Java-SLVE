public class SampleFile_1 {
    // フィールド変数
    private boolean a;
    private char b;

    // メインメソッド
    public static void main(String[] args) {
        SampleFile_1 ve = new SampleFile_1();
        ve.evaluateVariables(true, 'A');
    }

    // メソッド
    public void evaluateVariables(boolean x, char y) {
        // ローカル変数
        byte c = 10;
        short d = 20;
        int e = 30;
        float f = 3.14f;
        long g = 1000000L;
        double h = 2.71828;
        Object o = new Object();
        String s = "Sample";
        Exception t = new Exception("Error");

        // 一文字変数
        a = x;
        b = y;

        // 出力
        System.out.println("変数 a: " + a);
        System.out.println("変数 b: " + b);
        System.out.println("変数 c: " + c);
        System.out.println("変数 d: " + d);
        System.out.println("変数 e: " + e);
        System.out.println("変数 f: " + f);
        System.out.println("変数 g: " + g);
        System.out.println("変数 h: " + h);
        System.out.println("変数 o: " + o.toString());
        System.out.println("変数 s: " + s);
        System.out.println("変数 t: " + t.getMessage());

        // 配列
        int[] n = { 1, 2, 3, 4, 5 };
        for (int i = 0; i < n.length; i++) {
            System.out.println("n[" + i + "] = " + n[i]);
        }
    }
}