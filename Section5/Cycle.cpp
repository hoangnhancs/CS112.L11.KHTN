#include <bits/stdc++.h>
#define F(x) a[x].fa
using namespace std;
char s[1 << 20], ss[1 << 21];
int t, n;
struct SAM
{
    struct node
    {
        int ch[26], l, fa, tm;
    } a[1 << 21];
    int tot = 1, ls = 1, f[1 << 21];
    basic_string<int> v[1 << 21];
    void add(int c)
    {
        int p = ls, np = ls = ++tot;
        a[np].l = a[p].l + 1;
        v[a[np].l] += np;
        f[np] = 1;
        for (; p && !a[p].ch[c]; p = F(p))
            a[p].ch[c] = np;
        if (!p)
        {
            a[np].fa = 1;
            return;
        }
        int q = a[p].ch[c], nq;
        if (a[q].l == a[p].l + 1)
        {
            F(np) = q;
            return;
        }
        a[nq = ++tot] = a[q];
        v[a[nq].l = a[p].l + 1] += nq;
        F(q) = F(np) = nq;
        for (; p && a[p].ch[c] == q; p = F(p))
            a[p].ch[c] = nq;
    }
    void dp()
    {
        for (int i = n; i; i--)
            for (int j : v[i])
                f[F(j)] += f[j];
    }
    void dfs(int n, int tm)
    {
        int p = 1, cnt = 0, l = 0;
        for (int i = 1; i < 2 * n; i++)
        {
            while (p && !a[p].ch[ss[i] - 'a'])
                l = a[p = F(p)].l;
            if (!p)
            {
                puts("0");
                return;
            }
            l++, p = a[p].ch[ss[i] - 'a'];
            if (l == n && a[p].tm != tm)
                a[p].tm = tm, cnt += f[p];
            if (l == n)
                --l == a[F(p)].l && (p = F(p));
        }
        printf("%d\n", cnt);
    }
} S;
int main()
{
    scanf("%s%d", s + 1, &t);
    n = strlen(s + 1);
    for (int i = 1; i <= n; i++)
        S.add(s[i] - 'a');
    S.dp();
    while (t--)
    {
        scanf("%s", ss + 1);
        int m = strlen(ss + 1);
        strcpy(ss + m + 1, ss + 1);
        S.dfs(m, t + 1);
    }
    return 0;
}