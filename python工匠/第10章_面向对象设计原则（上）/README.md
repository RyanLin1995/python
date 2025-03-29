# SOLID 设计原则
> SOLID原则的雏形来自Robert C.Martin（Bob大叔）于2000年发表的一篇文章，其中他创造与整理了多条面向对象设计原则。在随后出版的《敏捷软件开发：原则、模式与实践》书中，Bob大叔提取了这些原则的首字母，组成了单词SOLID来帮助记忆。

SOLID单词里的5个字母，分别代表5条设计原则。
* S:single responsibility principle(单一职责原则，SRP)。
* O:open-closed principle(开放-关闭原则，OCP)。
* L:Liskov substitution principle(里式替换原则，LSP)。
* I:interface segregation principle(接口隔离原则，ISP)。
* D:dependency inversion principle(依赖倒置原则，DIP)。

在编写面向对象代码时，遵循这些设计原则可以帮你避开常见的设计陷阱，以便写出易于扩展的好代码。
反之，如果你的代码违反了其中某几条原则，那么你的设计可能有相当大的改进空间。

### 1.单一职责原则
单一职责原则(Single Responsibility Principle)，也称单一责任原则，是指一个类仅有一个被修改的理由。

换句话说：每个类都应该只承担一种职责。

最简单实现方式：
- 创建一个类，只包含一个方法。（大类拆分成小类）

### 2. 开放-关闭原则
开放-关闭原则(Open-Closed Principle)，也称开闭原则，是指对扩展开放，对修改关闭。

换句话说：你可以在不修改某个类的前提下，扩展它的行为。

最简单实现方式：
- 通过继承改造代码
- 使用组合与依赖注入
- 使用数据驱动：将经常变动的部分以数据的方式抽离出来，当需求变化时，只改动数据，代码逻辑可以保持不动。