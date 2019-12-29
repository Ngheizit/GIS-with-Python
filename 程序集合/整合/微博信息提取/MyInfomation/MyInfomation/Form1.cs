using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;

namespace MyInfomation
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            AddHeader("词汇");
            AddHeader("频数");
        }

        private void AddHeader(string text, int width = 100)
        {
            ColumnHeader colhdr = new ColumnHeader() { Text = text, Width = 100 };
            listView1.Columns.Add(colhdr);
        }
        private void AddTuple(params string[] strs)
        {
            ListViewItem item = new ListViewItem(strs);
            listView1.Items.Add(item);
        }
        private void InputTxt()
        {
            FileStream fs = new FileStream("word.txt", FileMode.OpenOrCreate, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.Default);
            int len = listView1.Items.Count;
            for (int i = 0; i < len; i++)
            {
                string text = listView1.Items[i].SubItems[0].Text;
                int count = Convert.ToInt32(listView1.Items[i].SubItems[1].Text);
                for (int j = 0; j < count; j++)
                {
                    int num = new Random().Next();
                    sw.WriteLine(text + " " + num.ToString());
                    sw.WriteLine(" ");
                }
            }
            sw.Close();
            fs.Close();
        }
        private void DrawWordCloud()
        {
            try
            {

                string[] strArr = new string[2] {
                    "word.txt", "extent.png"
                };
                RunPy(Application.StartupPath + @"\wxz_6_词云绘制.py", "", strArr);


            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString(), "错误信息");
            }
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            string text = textBox1.Text;
            string count = numericUpDown1.Value.ToString();
            AddTuple(text, count);
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            InputTxt();
            DrawWordCloud();
        }



        public static void RunPy(string filename, string args = "", params string[] teps)
        {
            string sArguments = filename;
            foreach (string sigstr in teps)
            {
                sArguments += " " + sigstr;//传递参数
            }
            sArguments += " " + args;

            ProcessStartInfo startInfo = new ProcessStartInfo()
            {
                FileName = "python.exe",
                Arguments = sArguments,
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardInput = true,
                RedirectStandardError = true,
                CreateNoWindow = true
            };
            Process p = new Process()
            {
                StartInfo = startInfo
            };
            p.Start();
            p.BeginOutputReadLine();
            p.WaitForExit();
        }
    }
}
