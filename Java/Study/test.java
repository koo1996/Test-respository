@GetMapping("/search") //검색창
    public ModelAndView search(String keyword) {
        List<InfoDTO> list = dao.searchM1(keyword);
        ModelAndView mav = new ModelAndView();
        if (list.size() != 0) {
            mav.addObject("list", list);
            mav.addObject("button", "메인화면");
        } else {
            mav.addObject("msg", "추출x");
        }
        mav.setViewName("mainPage");
        return mav;
    }