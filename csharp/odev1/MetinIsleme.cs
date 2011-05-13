using System;
using System.Collections;
using System.IO;
using Files;
using Others;
namespace Files {
	public class ReadWrite {
		public static string read(string dosyaYolu) {
			string readStr = "";
			StreamReader sr = new StreamReader(dosyaYolu);
			readStr = sr.ReadToEnd();
			sr.Close();
			return readStr;
		}
	}
}

namespace Others {
	public class MyStack {
	   int capacity;
	   string[] stack;
	   int top;
	   
	   public MyStack(int MaxElements) {
		   capacity = MaxElements;
		   stack = new string[capacity];
	   }
	   
	   public bool isEmpty() {
			if (top == 0)
				return true;
			return false;
	   }

	   public int push(string Element) {
		   if (top == capacity - 1)
			   return -1;
		   else {
			   stack[top++] = Element;
			   return top - 1;
		   }
	   }

	   public string pop() {
		   string RemovedElement;
		   string temp = null;
		   if (!(top <= 0)) {
				 RemovedElement = stack[top - 1];
				 top--;
				 return RemovedElement;
		   }
		   return temp;
	   }

	   public string peek() {
		string temp = null;
		if (top != 0)
			return stack[top - 1];
		else
			return temp;
	   }
	}
	
	public class ForText {
		public static ArrayList cozumle(string metin) {
			ArrayList str = new ArrayList();
			for(int i = 0; i < metin.Length; i++)
				if (metin[i] == '<' )
					if (metin[i + 1] != '/')
						str.Add(metin.Substring(i + 1, 1));
					else
						str.Add(metin.Substring(i + 1, 2));
			return str;
		}
		
		public static bool isAppr(ArrayList etiketler, int kapasite) {
			MyStack s = new MyStack(kapasite);
			bool balanced = true;
			int i = 0;
			string etiket, top;
			while (i < etiketler.Count && balanced) {
				etiket = etiketler[i] as string; 
				if (etiket[0] != '/')
					s.push(etiket);
				else
					if (s.isEmpty())
						balanced = false;
					else {
						top = s.peek();
						if ( top != etiket.Substring(1)) {
							balanced = false;
						}
						else {
							top = s.pop();
						}
					}
				i++;
			}
			
			if (balanced && s.isEmpty())
				return true;
			else
				return false;
		}
		
		public static string strUp(string str) {
			return str.ToUpper();
		}
		
		public static string repeat(string str) {
			return str + str;
		}
	}
}

namespace EveryThing {
	class MainPro {
		static void Main(string[] args) {
			int i, uf, bf, hf;
			bool control;
			string chStr, str;
			char ch;
			uf = 0;
			bf = 0;
			hf = 0;
			str = ReadWrite.read("kaynak.txt");
			control = ForText.isAppr(ForText.cozumle(str), 20);
			
			if (control) {
				for (i = 0; i < str.Length; i++)
					if (str[i] == '<') {
						ch = str[i + 1];
						if (ch != '/') {
							i += 2;
							if (ch == 'u') uf = 1;
							if (ch == 'b') bf = 1;
							if (ch == 'h') hf = 1;
							if (ch == 'p')
								if (hf !=1 && bf != 1)
									Console.Write("[");
								else if( bf == 1)
									Console.Write("[[");
						}
						
						else if (ch == '/') {
							ch = str[i + 2];
							i += 3;
							if (ch == 'u') uf = 0;
							if (ch == 'b') bf = 0;
							if (ch == 'h') hf = 0;
							if (ch == 'p')
								if (hf !=1 && bf != 1)
									Console.Write("]");
								else if(bf == 1)
									Console.Write("]]");
						}
					}
					
					else if (hf == 0) {
						chStr = Convert.ToString(str[i]);
						if (uf == 0 && bf == 0)
							Console.Write(str[i]);
						if (uf == 0 && bf == 1)
							Console.Write(ForText.repeat(chStr));
						if (uf == 1 && bf == 0)
							Console.Write(ForText.strUp(chStr));
						if (uf == 1 && bf == 1)
							Console.Write(ForText.strUp(ForText.repeat(chStr)));
					}
			}
			
			else
				Console.WriteLine("Kaynak dosyanın biçimleme etiketleri hatalıdır, kontrol ediniz!!!");
		}
	}
}
