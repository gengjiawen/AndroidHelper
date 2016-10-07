package ${packageName};

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.shundaojia.travel.R;
import com.shundaojia.travel.ui.base.BaseFragment;

import javax.inject.Inject;

import butterknife.ButterKnife;

public class ${className}Fragment extends BaseFragment implements ${className}MvpView {
    @Inject
    ${className}Presenter presenter;

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_${className?lower_case}, container, false);
        fragmentComponent().inject(this);
        ButterKnife.bind(view);

        presenter.attachView(this);

        return view;
    }

    @Override
    public void onDestroyView() {
        super.onDestroyView();
        presenter.detachView();
    }
}

