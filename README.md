# DoxAlign.vim

Align doxygen comments so that they look reasonable.

This is my first plugin, so it's probably very rough. Any feedback is welcome.

## Dependencies

- `glts/vim-textobj-comment.git`
- [optional] `yycho0108/vim-toop`

(Note that [`yycho0108/vim-toop`](https://github.com/yycho0108/vim-toop) is a fork of
[`jeanCarloMachado/vim-toop`](https://github.com/jeanCarloMachado/vim-toop) with a minor change)


## Configuration

In your `~/.vimrc`:

```vim
" For comment text object
Plugin 'glts/vim-textobj-comment.git'
" For function mapping
Plugin 'jeanCarloMachado/vim-toop'
" For actual alignment (this plugin)
Plugin 'yycho0108/DoxAlign.vim'
"

" Add mapping ...
call toop#mapFunction('DoxAlign', "<leader>da")"
```

## How to use

Now, pressing `vac<leader>da` or `<leader>daac` will format the comment object under the cursor.

(A mapping like `<leader>daac` will only work with the forked `vim-toop` repo, due to repeated `a` character)

## Sample

Random text generated from [here](https://www.weirdhat.com/gibberish.php).

The same file can be seen in the [sample text](./python/sample.txt)

Input:

```
  /**
   * @brief   Sosec cariege nep opo rarur lewu serise tek cinicer.  
   * Sagis eni mole ilon ginerep hotaroh ge. Can isoda tel. Ulorienel lie igateca
   * yonedal dace.
   *
   * Ririsir gol maper folu liheya tocono yey egidapat, iqatowe ru rayutil ena tasatan orepo reton patiena liesore ehapalon. Lipar fesa rido amesede ohemuwen nes tecin ni racera. Sohera ronal ye cepeg cos. Ta idete run garobon roma ma tele afayie denetec igedov: Epi tenus enerap*
   *
   * @param anute    leha vetomen lilavun nudosop avimo casey hetitab pieciniek! Zuga lo moseco obeca nohepe! Ca esosar ope cog roh eta. Tu igumon rogepam yo nuce cihenod laheh yon; bocit alewec sut ran ya. Regir bepesic co sorile lor yi cedenor yasey etoloham edi! So lapa rosit buler die oraral risa ili. 
   *   @param[out] tata efe wi tonaro solovos le fosi ahohox sabe mi. Ieto cesafe got cadegu li eti toriyu res. Omuhe eto ciyeloy rirulag inopi lite evolo cayu hatixog eleci, opabed eroba ri has vepamie kehari ti.
   * @return Biroz na visoc wa nabem sa; huroli ho eciyab 
   *
   */
```

Output:

```
  /**
   * @brief      Sosec cariege nep opo rarur lewu serise tek cinicer. Sagis eni
   *             mole ilon ginerep hotaroh ge. Can isoda tel. Ulorienel lie
   *             igateca yonedal dace.
   * 
   * Ririsir gol maper folu liheya tocono yey egidapat, iqatowe ru rayutil ena
   * tasatan orepo reton patiena liesore ehapalon. Lipar fesa rido amesede
   * ohemuwen nes tecin ni racera. Sohera ronal ye cepeg cos. Ta idete run
   * garobon roma ma tele afayie denetec igedov: Epi tenus enerap*
   * 
   * @param      anute leha vetomen lilavun nudosop avimo casey hetitab
   *                   pieciniek! Zuga lo moseco obeca nohepe! Ca esosar ope cog
   *                   roh eta. Tu igumon rogepam yo nuce cihenod laheh yon;
   *                   bocit alewec sut ran ya. Regir bepesic co sorile lor yi
   *                   cedenor yasey etoloham edi! So lapa rosit buler die
   *                   oraral risa ili.
   * @param[out] tata  efe wi tonaro solovos le fosi ahohox sabe mi. Ieto cesafe
   *                   got cadegu li eti toriyu res. Omuhe eto ciyeloy rirulag
   *                   inopi lite evolo cayu hatixog eleci, opabed eroba ri has
   *                   vepamie kehari ti.
   * 
   * @return           Biroz na visoc wa nabem sa; huroli ho eciyab
   */

```

&copy; 2020, Yoonyoung Cho, All rights reserved.
